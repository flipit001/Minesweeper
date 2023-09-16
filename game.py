import sys, pygame
from pygame.locals import *

sys.path.append("src/")
from src.vars import *
from src.sudokuenv import *

dif = sys.argv[1].lower()

env = SudokuEnv(dif)
env._print_board()
num_size = CALC_NUMBER_SIZE(env.size[0], env.size[1])

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont("arial", size=36)
button_screen = pygame.surface.Surface((WIDTH, 200))
tile_screen = pygame.surface.Surface((WIDTH, HEIGHT - 200))
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

        tile_screen.fill("white")

        pygame.display.flip()

pygame.quit()
