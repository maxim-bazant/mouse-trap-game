from settings import *
import time
import pygame


class Door(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.closed_door = pygame.image.load("images/door/closed_door.png").convert_alpha()
        self.opened_door = pygame.image.load("images/door/opened_door.png").convert_alpha()

        self.animation = []
        for number in ["01", "02", "03", "04", "closed_door"]:
            self.animation.append(pygame.image.load(f"images/door/{number}.png"))

        self.width = self.closed_door.get_rect().width
        self.height = self.closed_door.get_rect().height
        self.open = False
        self.mask = pygame.mask.from_surface(self.opened_door)
        self.mouse_into_door_count = 0
        self.mouse_done_going_into_door = False
        self.image_changer = 15

    def show_me(self, balls):
        if len(balls) != 0:
            win.blit(self.closed_door, (self.x, self.y))
            self.open = False
        else:
            win.blit(self.opened_door, (self.x, self.y))
            self.open = True

    def mouse_going_into_door(self):
        if self.mouse_into_door_count + 1 < len(self.animation) * self.image_changer:
            self.mouse_into_door_count += 1

            win.blit(self.animation[self.mouse_into_door_count // self.image_changer], (self.x, self.y))

        else:
            self.mouse_into_door_count = 0
            self.mouse_done_going_into_door = True



