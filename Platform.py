import pygame
from settings import *


class Platform:
    def __init__(self, image, x, y):
        self.image = image.convert_alpha()
        self.x = x
        self.y = y
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def blit(self):
        win.blit(self.image, (self.x - self.width, self.y))
