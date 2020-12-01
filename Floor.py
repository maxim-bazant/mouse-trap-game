import pygame
from settings import *


class HorizontalFloor:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

