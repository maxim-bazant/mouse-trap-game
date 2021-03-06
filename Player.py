import pygame
import decimal
import time
from settings import *


class Player:
    def __init__(self):
        self.play_jump_sound = False
        self.right_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.right_images.append(pygame.image.load(f"images/mouse/right/{number}.png").convert_alpha())

        self.left_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"images/mouse/left/{number}.png").convert_alpha())

        self.dying_images = []
        for number in ["01", "02", "01", "02", "01", "02", "01", "02", "01", "02", "01", "02",
                       "03", "04", "05", "06", "07", "07"]:
            self.dying_images.append(pygame.image.load(f"images/mouse/dying/{number}.png").convert_alpha())

        self.image_changer = 7
        self.dying_image_changer = 20

        self.play_death_sound = True

        self.mask = pygame.mask.from_surface(self.left_images[0])

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

        self.x = win_width - self.width - 20  # 20 to not the edge
        self.y = 150

        self.vel = 3
        self.jumping_vel = 3.5

        self.lives = 4

        self.acc = 3

        self.facing_right = False
        self.facing_left = True

        self.walk_count = 0
        self.walking = True

        self.dying_count = 0
        self.dying = False
        self.done_dying = True

        self.going_into_door = False

        self.can_walk_left = True
        self.can_walk_right = True

        self.jumping = False
        self.jump_count = 4.5
        self.can_not_jump = False
        self.no_jump_up = False

        self.falling = False
        self.reducing_y = False

        self.fall_damage_count = 0
        self.die_bc_fall_damage = False

        self.move_left_bc_tha_wall = False
        self.move_right_bc_tha_wall = False

    def move_right(self):
        self.facing_right = True
        self.facing_left = False
        self.x += self.vel

    def move_left(self):
        self.facing_left = True
        self.facing_right = False
        self.x -= self.vel

    def jump(self, play_jump_sound):
        self.jumping = True
        self.play_jump_sound = play_jump_sound

        if self.jumping:
            if self.play_jump_sound:
                self.play_jump_sound = False
                jump_sound.play()

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

    def blit_dying(self):
        if self.play_death_sound:
            dying_sound.play()
            self.play_death_sound = False

        self.done_dying = False
        self.dying_image_changer = 9
        if self.dying_count + 1 < self.dying_image_changer * len(self.dying_images):
            self.dying_count += 1
        else:
            self.dying_count = 0

        self.mask = pygame.mask.from_surface(self.dying_images[self.dying_count // self.dying_image_changer])
        win.blit(self.dying_images[self.dying_count // self.dying_image_changer], (self.x, self.y))

        if self.dying_count // self.dying_image_changer == 17:
            self.move_left_bc_tha_wall = False
            self.move_right_bc_tha_wall = False
            self.facing_right = False
            self.facing_left = True
            self.dying = False
            self.dying_count = 0
            self.x = win_width - self.width - 20
            self.y = 150
            self.dying_image_changer = 10
            self.jumping = False
            self.jump_count = 4.5
            self.done_dying = True
            self.lives -= 1
            self.die_bc_fall_damage = False
            self.play_death_sound = True

            time.sleep(0.25)

    def reset(self):
        self.going_into_door = False
        self.facing_right = False
        self.facing_left = True
        self.x = win_width - self.width - 20
        self.y = 150
        self.jumping = False
        self.jump_count = 4.5
        self.lives = 4

