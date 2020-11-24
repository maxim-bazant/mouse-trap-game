from settings import *
import pygame


class RedFloorTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/floor/red_floor_tile.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.list_of_tile = []
        self.mask = pygame.mask.from_surface(self.image)

    def show(self):
        win.blit(self.image, (self.x, self.y))


