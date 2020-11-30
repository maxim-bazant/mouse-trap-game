import pygame
from settings import *


class Player:
    def __init__(self):
        self.right_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.right_images.append(pygame.image.load(f"images/mouse/right/{number}.png").convert_alpha())

        self.left_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"images/mouse/left/{number}.png").convert_alpha())

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

        self.x = win_width - self.width - 20  # 20 to not the edge
        self.y = 200
        self.vel = 5

        self.facing_right = False
        self.facing_left = True

        self.walk_count = 0
        self.walking = True

    def move_right(self):
        self.facing_right = True
        self.facing_left = False
        self.x += self.vel

    def move_left(self):
        self.facing_left = True
        self.facing_right = False
        self.x -= self.vel

    def jump(self):
        pass

    def stand(self):
        if self.facing_left:
            win.blit(self.left_images[0], (self.x, self.y))
        elif self.facing_right:
            win.blit(self.right_images[0], (self.x, self.y))

