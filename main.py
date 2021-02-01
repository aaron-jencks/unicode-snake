import os
import random as rnd
import time

import kbutils as kb


class SnakeBoard:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.vertices = []
        self.odd_column = False

        self.buff = []
        for _ in range(self.rows):
            self.buff.append([' ' for _ in range(self.columns)])

    def initialize(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.buff[r][c] = ' '
        self.odd_column = (self.columns >> 1) % 2 == 1
        self.buff[self.rows >> 1][self.columns >> 1] = '\u25cb'
        self.vertices = [(self.rows >> 1, self.columns >> 1)]

    def place_food(self):
        while True:
            r = rnd.randint(0, self.rows - 1)
            c = rnd.randint(0, self.columns - 1)
            codd = c % 2 == 1
            if (codd and self.odd_column or not codd and not self.odd_column) and self.buff[r][c] != '\u25cb':
                self.buff[r][c] = '\u25c9'
                break

    def tick(self, direction: int) -> bool:
        nr, nc = self.vertices[-1]

        if direction == 0:
            nr -= 1
        elif direction == 1:
            nc += 2
        elif direction == 2:
            nr += 1
        elif direction == 3:
            nc -= 2
        else:
            print("Invalid direction for snake")
            exit(1)

        if nr >= self.rows or nc >= self.columns or nr < 0 or nc < 0 or self.buff[nr][nc] == '\u25cb':
            return False

        self.vertices.append((nr, nc))
        self.vertices.pop(0)
        return True


class SnakeGame(SnakeBoard):
    def __init__(self, rows: int, columns: int):
        super().__init__(rows, columns)
        self.score = 0
        self.direction = 0
        self.initialize()
        self.place_food()

    def tick(self, direction: int = -1) -> bool:
        v = super().tick(self.direction if direction < 0 else direction)

        if self.buff[self.vertices[-1][0]][self.vertices[-1][1]] == '\u25c9':
            self.score += 1
            self.vertices.append(self.vertices[-1])
            self.place_food()

        for r in range(self.rows):
            for c in range(self.columns):
                if (r, c) in self.vertices:
                    self.buff[r][c] = '\u25cb'
                elif self.buff[r][c] != '\u25c9' and self.buff[r][c] != ' ':
                    self.buff[r][c] = ' '
        return v

    def __str__(self):
        result = ''
        for r in self.buff:
            for c in r:
                result += c
            result += '\033[E'
        return result + 'Score: {}'.format(self.score)


if __name__ == '__main__':
    size = os.get_terminal_size()
    game = SnakeGame(size.lines - 1, size.columns)

    print("\033[2J\033[H{}", game)
    time.sleep(1 / 10)

    while True:
        k = kb.get_char()

        if k == 'a':
            game.direction = 3
        elif k == 's':
            game.direction = 2
        elif k == 'd':
            game.direction = 1
        elif k == 'w':
            game.direction = 0

        if game.tick():
            print("\033[2J\033[H{}", game)
            time.sleep(1 / ((int(game.score / 10 + 1)) * 10))
        else:
            print("\033[2J\033[HGame Over!\nScore: {}".format(game.score))
            r = input("Would you like to play again?: ")
            if r[0] == 'y' or r[0] == 'Y':
                game.initialize()
                game.place_food()
                game.score = 0
                continue
            break
