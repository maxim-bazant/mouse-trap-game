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

        self.image_changer = 3

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

        self.x = win_width - self.width - 20  # 20 to not the edge
        self.y = 200
        self.vel = 7
        self.jumping_vel = 5

        self.acc = 3

        self.facing_right = False
        self.facing_left = True

        self.walk_count = 0
        self.walking = True

        self.jumping = False
        self.jump_count = 5.25

        self.falling = False

        self.mask = None

    def move_right(self):
        if not self.jumping:
            self.facing_right = True
            self.facing_left = False
            self.x += self.vel

            self.blit_moving_right()

    def move_left(self):
        if not self.jumping:
            self.facing_left = True
            self.facing_right = False
            self.x -= self.vel

            self.blit_moving_left()

    def jump(self):
        self.jumping = True

        if self.jumping:
            if self.jump_count >= -5.25:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 0.25
            else:
                self.jump_count = 5.25
                self.jumping = False
                self.walking = True

            if self.facing_left:
                win.blit(self.left_images[0], (self.x, self.y))
            elif self.facing_right:
                win.blit(self.right_images[0], (self.x, self.y))

    def blit_moving_right(self):
        if self.walk_count + 1 < self.image_changer * len(self.right_images):
            self.walk_count += 1
        else:
            self.walk_count = 0

        win.blit(self.right_images[self.walk_count // self.image_changer], (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.right_images[self.walk_count // self.image_changer])

    def blit_moving_left(self):
        if self.walk_count + 1 < self.image_changer * len(self.left_images):
            self.walk_count += 1
        else:
            self.walk_count = 0

        win.blit(self.left_images[self.walk_count // self.image_changer], (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.left_images[self.walk_count // self.image_changer])

    def blit_standing(self):
        if not self.walking:
            if self.facing_left:
                win.blit(self.left_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.left_images[0])
            elif self.facing_right:
                win.blit(self.right_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.right_images[0])

