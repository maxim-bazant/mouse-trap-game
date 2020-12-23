import pygame
from settings import *


class Piston(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/piston.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)
        self.mc_default = 250
        self.move_count = self.mc_default
        self.vel = 1.5

    def show_me(self):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        print(self.move_count)
        neg = 1
        if self.move_count >= self.mc_default // 2:
            neg = -1
        elif self.move_count <= self.mc_default // 2:
            neg = 1
        if self.move_count == 0:
            self.move_count = self.mc_default

        self.move_count -= 1
        self.y -= self.vel * neg

        self.show_me()
