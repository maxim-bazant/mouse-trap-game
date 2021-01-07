from settings import *
from settings import FPS as FPS


class Tail(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/piston_tail.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_tail(self):
        win.blit(self.image, (self.x, self.y))


class Piston(object):
    def __init__(self, x, y, tail_count):
        self.x = x
        self.y = y
        self.starting_y = 311.5
        self.image = pygame.image.load("images/piston.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.vel = 1.5
        self.neg = 1  # 1 is for going down, -1 will be for going up
        self.tail = [Tail(self.x + self.width // 2 - 12, self.starting_y)]
        self.mask = pygame.mask.from_surface(self.image)
        self.first_time = True
        self.first_count = 0
        self.tail_count = tail_count

    def show_and_move(self, player):
        if self.first_time:
            while self.first_count < self.tail_count:
                self.show_tail(self.neg)

            self.first_time = False

        else:
            self.show_tail(self.neg)

        win.blit(self.image, (self.x, self.y))

        if not player.dying:
            if self.y > 500:
                self.neg = -1
            elif self.y < self.starting_y:
                self.neg = 1

            self.y += self.vel * self.neg

    def show_tail(self, neg):
        for tail in self.tail:
            tail.show_tail()

        if self.y - (self.tail[-1].y + self.tail[-1].height) > -5 and neg == 1:
            self.tail.append(Tail(self.tail[-1].x, self.tail[-1].y + self.tail[-1].height))
        elif self.y - self.tail[-1].y < -5 and neg == -1:
            self.tail.pop(-1)
        self.first_count += 1
