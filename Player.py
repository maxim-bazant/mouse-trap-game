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

        self.image_changer = 6

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

        self.x = win_width - self.width - 20  # 20 to not the edge
        self.y = 200

        self.vel = 4
        self.jumping_vel = 3

        self.acc = 5

        self.facing_right = False
        self.facing_left = True

        self.walk_count = 0
        self.walking = True

        self.can_walk_left = True
        self.can_walk_right = True

        self.jumping = False
        self.jump_count = 4.5
        self.can_not_jump = False
        self.no_jump_up = False

        self.falling = False
        self.reducing_y = False

        self.move_a_little_bit = False

    def move_right(self):
        self.facing_right = True
        self.facing_left = False
        self.x += self.vel

    def move_left(self):
        self.facing_left = True
        self.facing_right = False
        self.x -= self.vel

    def jump(self):
        self.jumping = True

        if self.jumping:
            if self.jump_count >= -4.5:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                    self.reducing_y = True
                self.y -= round((self.jump_count ** 2) * 0.5 * neg)
                self.jump_count -= 0.15
            else:
                self.reducing_y = False
                self.jump_count = 4.5
                self.jumping = False
                self.walking = True

            if self.facing_left:
                win.blit(self.left_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.left_images[0])
            elif self.facing_right:
                win.blit(self.right_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.right_images[0])

    def blit_moving_right(self):
        if self.walk_count + 1 < self.image_changer * len(self.right_images):
            self.walk_count += 1
        else:
            self.walk_count = 0

        self.mask = pygame.mask.from_surface(self.right_images[self.walk_count // self.image_changer])
        win.blit(self.right_images[self.walk_count // self.image_changer], (self.x, self.y))

    def blit_moving_left(self):
        if self.walk_count + 1 < self.image_changer * len(self.left_images):
            self.walk_count += 1
        else:
            self.walk_count = 0

        self.mask = pygame.mask.from_surface(self.left_images[self.walk_count // self.image_changer])
        win.blit(self.left_images[self.walk_count // self.image_changer], (self.x, self.y))

    def blit_standing(self):
        if not self.walking:
            if self.facing_left:
                win.blit(self.left_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.left_images[0])
            elif self.facing_right:
                win.blit(self.right_images[0], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.right_images[0])

