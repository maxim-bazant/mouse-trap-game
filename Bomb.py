from settings import *
import pygame
import random


class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/bomb/dot.png")

    def show_me(self):
        win.blit(self.image, (self.x, self.y))


class Bomb(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/bomb/bomb.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.dot_x = self.x + self.width - 54  # 44
        self.dot_y = self.y - 4
        self.tail = []
        self.make_tail()
        self.bomb_count = 0
        self.explode_ = False
        self.exploded_already = False
        self.speed = 100
        self.sparkle_count = 0
        self.explode_count = 0
        self.image_changer = 15
        self.explosion_image_changer = 20

        self.sparkles = []
        for number in ["01", "02", "03", "04"]:
            self.sparkles.append(pygame.image.load(f"images/bomb/sparkles_{number}.png").convert_alpha())

        self.explosion = []
        for number in ["01", "02", "03", "04", "05"]:
            self.explosion.append(pygame.image.load(f"images/bomb/explosion_{number}.png").convert_alpha())

    def show_me(self):
        if not self.explode_:
            win.blit(self.image, (self.x, self.y))
        for dot in self.tail:
            dot.show_me()

        if self.bomb_count % self.speed == 0 and self.tail != []:
            self.tail.pop(-1)
        elif not self.tail:
            self.explode_ = True
            self.explode()

        self.bomb_count += 1

        if self.tail:
            if self.sparkle_count + 1 < len(self.sparkles) * self.image_changer:
                self.sparkle_count += 1
            else:
                self.sparkle_count = 0

            win.blit(self.sparkles[self.sparkle_count // self.image_changer], (self.tail[-1].x - 25, self.tail[-1].y - 25))

    def make_tail(self):
        for i in range((win_height - 300) // 4):
            self.tail.append(Dot(self.dot_x, self.dot_y))

            number = random.randint(0, 3)
            if number == 0:
                if self.dot_x > self.x + self.width - 110:
                    self.dot_x -= 4
                else:
                    self.dot_x += 4
            elif number == 1:
                if self.dot_x < self.x + self.width - 4:
                    self.dot_x += 4
            elif number == 2:
                self.dot_x += 0
            elif number == 3:
                self.dot_x += 0

            self.dot_y -= 4

    def explode(self):
        if self.explode_:
            if self.explode_count + 1 < len(self.explosion) * self.explosion_image_changer:
                self.explode_count += 1
            else:
                self.explode_count = 0
                self.exploded_already = True

            if self.exploded_already:
                win.blit(self.explosion[-1], (self.x - 25, self.y - 25))
            else:
                win.blit(self.explosion[self.explode_count // self.explosion_image_changer], (self.x - 25, self.y - 25))
