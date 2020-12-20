from settings import *
import pygame


class FallingFloor(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/floor/falling_floor.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.fall_count = 0

    def show_me(self):
        win.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y += 0.5
        self.fall_count += 1
