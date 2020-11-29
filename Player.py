import pygame
from Game import *


class Player(object):
    def __init__(self):
        self.x = win_width - self.width
        self.y = 200
        self.right_images = []
        self.left_images = []
        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height
        self.vel = 5
        self.moving_left = True
        self.moving_right = False

    def move_right(self):
        self.moving_right = True
        self.x += self.vel
        self.blit_me()

    def move_left(self):
        self.moving_right = True
        self.x -= self.vel
        self.blit_me()

    def blit_me(self):
        if self.moving_right:
            pass
        elif self.moving_left:
            pass






















