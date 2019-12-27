from constants import *
from classes import *
import pygame


class Game:
    def __init__(self):
        self.field = Field(N, M)
        self.running = False

    def run(self):
        pygame.init()
        self.win = pygame.display.set_mode((SZX, SZY))
        self.running = True

        while self.running:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.running = False
                if i.type == pygame.MOUSEBUTTONDOWN:
                    self.field.click(*get_xy_by_click(*i.pos))
            self.show()
            pygame.display.update()

    def show(self):
        for i in range(self.field.n):
            for j in range(self.field.m):
                pygame.draw.rect(self.win, self.field.cells[i][j].color.to_c(), (i * sz, j * sz, sz, sz))

