from settings import *
import pygame


class Door(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.closed_door = pygame.image.load("images/door/closed_door.png").convert_alpha()
        self.opened_door = pygame.image.load("images/door/opened_door.png").convert_alpha()
        self.width = self.closed_door.get_rect().width
        self.height = self.closed_door.get_rect().height
        self.open = False

    def show_me(self, balls):
        if len(balls) != 0:
            win.blit(self.closed_door, (self.x, self.y))
            self.open = False
        else:
            win.blit(self.opened_door, (self.x, self.y))
            self.open = True


