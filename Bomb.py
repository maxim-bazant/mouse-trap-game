from settings import *
import pygame
import random


class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/dot.png")

    def show_me(self):
        win.blit(self.image, (self.x, self.y))


class Bomb(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/bomb.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.dot_x = self.x + self.width - 54  # 44
        self.dot_y = self.y - 4
        self.tail = []
        self.make_tail()
        self.bomb_count = 0
        self.explode = False

    def show_me(self):
        win.blit(self.image, (self.x, self.y))
        for dot in self.tail:
            dot.show_me()

        if self.bomb_count % 150 == 0 and self.tail != []:
            self.tail.pop(-1)
        elif not self.tail:
            self.explode = True

        self.bomb_count += 1

    def make_tail(self):
        for i in range((win_height - 300) // 4):
            self.tail.append(Dot(self.dot_x, self.dot_y))

            number = random.randint(0, 3)
            if number == 0:
                if self.dot_x > self.x + self.width - 120:
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
