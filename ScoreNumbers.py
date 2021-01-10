from settings import *
import pygame


class ScoreNumbers(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.numbers = []
        for number in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]:
            self.numbers.append(pygame.image.load(f"images/numbers/{number}.png").convert_alpha())

        self.width = self.numbers[0].get_rect().width
        self.height = self.numbers[1].get_rect().height

    def show_me(self, number):
        win.blit(self.numbers[number], (self.x, self.y))
