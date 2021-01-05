from settings import *
import pygame


class Ladder(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/ladder.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_me(self):
        win.blit(self.image, (self.x, self.y))
