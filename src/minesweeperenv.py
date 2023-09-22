from vars import *
from helpers import *
import random


class MinesweeperEnv:
    def __init__(self, difficulty):
        self.size, self.num_mines = TILES[difficulty]
        self.board = [[BLANK for _ in range(self.size[1])] for _ in range(self.size[0])]
        self.mine_count = 0
        self._add_random_mines()
        self._add_values()

    def __repr__(self):
        return str(self.board)

    def _coord_in_bounds(self, coord: tuple):
        x, y = coord
        return not (
            (x < 0 or x >= len(self.board[0])) or (y < 0 or y >= len(self.board))
        )

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
                            if not self._coord_in_bounds((x, y)):
                                continue
                            if self.board[y][x] != MINE:
                                self.board[y][x] += 1
                                # print(y, x)

    def all_revealed(self, coord):
        if self.board[coord[0]][coord[1]] != 0:
            print([coord])
            return [coord]
        output = []
        queue = CustomQueue()
        queue.append(coord)
        print(queue.length())
        while queue.length() > 0:
            # print("HERE")
            curpos = queue.pop()
            output.append(curpos)
            for operation in T_OPERATIONS:
                pos = t_addition(curpos, operation)
                if self._coord_in_bounds(pos) and self.board[pos[0]][pos[1]] == 0:
                    # print("HERE")
                    queue.append(pos)
                elif self._coord_in_bounds(pos):
                    output.append(pos)
        print(output)
        return output


if __name__ == "__main__":
    env = MinesweeperEnv("easy")
    env._print_board()
    x = int(input())
    y = int(input())
    env.all_revealed((x, y))
