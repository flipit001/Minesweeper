import sys
from src.vars import *
from src.sudokuenv import *

dif = sys.argv[1].lower()

env = SudokuEnv(dif)
env._print_board()
