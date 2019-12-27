from colors import *
from random import randrange as rd


class Cell:
    def __init__(self, color_id):
        self.color_id = color_id
        self.color = COLORS[color_id]

    def inverse_color(self):
        self.color_id = (self.color_id + 1) % 2
        self.color = COLORS[self.color_id]
        return self.color_id

    def change_color(self, color_id):
        self.color_id = color_id
        self.color = COLORS[self.color_id]

    def __str__(self):
        return str(self.color_id)


class Field:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.create_cells()

    def create_random_cells(self):
        self.cells = []
        for i in range(self.n):
            self.cells.append([])
            for j in range(self.m):
                self.cells[-1].append(Cell(rd(0, 2)))

    def create_cells(self):
        self.cells = []
        for i in range(self.n):
            self.cells.append([])
            for j in range(self.m):
                self.cells[-1].append(Cell(1))

    def click(self, x, y):
        for i in range(self.n):
            for j in range(self.m):
                if i == x or j == y:
                    self.cells[i][j].inverse_color()
                    print(i, j)

    def __str__(self):
        ret = ''
        for i in range(self.n):
            for j in range(self.m):
                ret += str(self.cells[i][j]) + ' '
            ret += '\n'
        return ret


if __name__ == '__main__':
    field = Field(5, 5)
    print(field)
