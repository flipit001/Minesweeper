import sys, pygame
from pygame.locals import *

sys.path.append("src/")
from src.vars import *
from src.sudokuenv import *
from src.interface import *

dif = sys.argv[1].lower()

env = SudokuEnv(dif)
env._print_board()
num_size = (WIDTH // env.size[0], (HEIGHT - START) // env.size[1])

pygame.init()

square = pygame.image.load("assets/square.png")
square = pygame.transform.scale(square, num_size)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont("arial", size=36)
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

        screen.fill("lightgray")

        for i in range(len(env.board)):
            for j in range(len(env.board[i])):
                # print(env.size[0] * i, env.size[1] * j)
                screen.blit(
                    square,
                    (num_size[0] * i, num_size[1] * j + START),
                )
        for i in range(len(env.board)):
            pygame.draw.aaline(
                screen,
                "black",
                (i * num_size[0], START),
                (i * num_size[0], HEIGHT),
            )
        for i in range(len(env.board[0])):
            pygame.draw.aaline(
                screen,
                "black",
                (0, i * num_size[1] + START),
                (WIDTH, i * num_size[1] + START),
            )

        pygame.display.flip()

pygame.quit()
