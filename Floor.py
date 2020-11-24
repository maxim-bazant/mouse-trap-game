import pygame


class RedFloorTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/floor/red_floor_tile.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

