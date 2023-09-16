from vars import *
from sudokuenv import *
import sys

dif = sys.argv[1].lower()

env = SudokuEnv(dif)
env._print_board()
