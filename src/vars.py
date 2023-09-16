TILES = {
    "easy": ((9, 9), 10),
    "medium": ((16, 16), 40),
    "hard": ((30, 16), 99),
}
BLANK = 0
MINE = -1
NUMBER_MODE = True
WIDTH, HEIGHT = 600, 800
CALC_NUMBER_SIZE = lambda nx, ny: (WIDTH // nx, (HEIGHT - 200) // ny)
