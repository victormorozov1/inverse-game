from random import randrange as rd
from functions import *


def rd_color():
    return rd(0, 256)


class Color:
    def __init__(self, r=rd_color(), g=rd_color(), b=rd_color()):
        self.r = r
        self.g = g
        self.b = b

    def __sub__(self, other):
        return abs(self.r - other.r) + abs(self.b - other.b) + abs(self.g - other.g)

    def set_random_color(self):
        self.r = rd_color()
        self.g = rd_color()
        self.b = rd_color()

    def to_c(self):
        return self.r, self.g, self.b

    def __str__(self):
        return 'Class Color r={}, g={}, b={}'.format(self.r, self.g, self.b)


MIN_COLOR_DIFF = 155
COLORS = [Color(), Color()]
while COLORS[0] - COLORS[1] < MIN_COLOR_DIFF:
    COLORS[1].set_random_color()
