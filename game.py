import sys, pygame
from pygame.locals import *

sys.path.append("src/")
from src.vars import *
from src.sudokuenv import *
from src.interface import *


class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.dif = sys.argv[1].lower()

        self.env = SudokuEnv(self.dif)
        self.env._print_board()
        self.num_size = (
            WIDTH // self.env.size[0],
            (HEIGHT - START) // self.env.size[1],
        )

        pygame.init()

        self.smile = pygame.image.load("assets/smile-icon.png")
        self.smile = pygame.transform.scale(self.smile, (100, 100))
        self.smile_button = Button(self.smile, WIDTH / 2, 50, self.reset)

        self.square = pygame.image.load("assets/square.png")
        self.square = pygame.transform.scale(self.square, self.num_size)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper")

        font = pygame.font.SysFont("arial", size=24)

        self.buttons = [[None for _ in self.env.board] for _ in self.env.board[0]]
        self.dead = False

        for i in range(len(self.env.board)):
            for j in range(len(self.env.board[i])):
                rect = pygame.rect.Rect(
                    (self.num_size[0] * i, self.num_size[1] * j + START), self.num_size
                )
                render = render_text(
                    font, str(self.env.board[i][j]), "black", "lightgray"
                )
                but = TileButton(render, rect, active=False, dif=self.dif)
                self.buttons[j][i] = but

    def run(self):
        running = True
        while running:
            ##############
            # event loop #
            ##############
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if not self.dead:
                        for i in range(len(self.buttons)):
                            for j in range(len(self.buttons[i])):
                                if (
                                    self.buttons[j][i].update(pygame.mouse.get_pos())
                                    and self.env.board[i][j] == -1
                                ):
                                    # print("HERE", j, i, self.env.board[i][j])
                                    self.dead = True

                    self.smile_button.update(pygame.mouse.get_pos())

                self.screen.fill("lightgray")

                # DRAW BOARD################################################################
                for i in range(len(self.env.board)):
                    for j in range(len(self.env.board[i])):
                        # print(self.env.size[0] * i, self.env.size[1] * j)
                        if self.buttons[j][i].active:
                            continue
                        self.screen.blit(
                            self.square,
                            (self.num_size[0] * i, self.num_size[1] * j + START),
                        )
                for i in range(len(self.env.board)):
                    pygame.draw.aaline(
                        self.screen,
                        "black",
                        (i * self.num_size[0], START),
                        (i * self.num_size[0], HEIGHT - 8),
                    )
                for i in range(len(self.env.board[0]) + 1):
                    pygame.draw.aaline(
                        self.screen,
                        "black",
                        (0, i * self.num_size[1] + START),
                        (WIDTH, i * self.num_size[1] + START),
                    )
                for i in range(len(self.env.board)):
                    for j in range(len(self.env.board[i])):
                        self.buttons[j][i].draw(self.screen)
                ###################################################################
                # draw buttons
                self.smile_button.draw(self.screen)

                pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()
