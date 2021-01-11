from settings import *
import pygame


class Life(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/life_image.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_me(self):
        win.blit(self.image, (self.x, self.y))

