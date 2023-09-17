from src.vars import *
import random


class SudokuEnv:
    def __init__(self, difficulty):
        self.size, self.num_mines = TILES[difficulty]
        self.board = [[BLANK for _ in range(self.size[1])] for _ in range(self.size[0])]
        self.mine_count = 0
        self._add_random_mines()
        self._add_values()

    def __repr__(self):
        return str(self.board)

    def _print_board(self):
        for row in self.board:
            print(row)

    def _add_random_mines(self):
        while self.mine_count < self.num_mines:
            indx, indy = (
                random.randint(0, self.size[0] - 1),
                random.randint(0, self.size[1] - 1),
            )
            # print(indx, indy, self.size)
            if self.board[indx][indy] != MINE:
                self.board[indx][indy] = MINE
                self.mine_count += 1

    def _add_values(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == MINE:
                    for x in range(j - 1, j + 2):
                        for y in range(i - 1, i + 2):  # get a box around the point
                            # print(i, j, x, y)
                            # print(len(self.board[0]))
                            if (x < 0 or x >= len(self.board[0])) or (
                                y < 0 or y >= len(self.board)
                            ):
                                continue
                            if self.board[y][x] != MINE:
                                self.board[y][x] += 1
                                print(y, x)
