import pygame
from settings import *


class HorizontalFloor:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)

        #  when showing floor take off self.x self.width and from self.y self.height
    def blit(self):
        win.blit(self.image, (self.x - self.width, self.y))
