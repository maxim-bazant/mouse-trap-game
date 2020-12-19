from settings import *
import pygame


class FallingFloor(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/floor/falling_floor.png")

    def show_me(self):
        win.blit(self.image, (self.x, self.y))

