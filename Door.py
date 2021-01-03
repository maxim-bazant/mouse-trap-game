from settings import *
import pygame


class Door(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_me(self):
        win.blit(self.image, (self.x, self.y))


