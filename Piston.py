from settings import *


class Tail(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/piston_tail.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def show_tail(self):
        win.blit(self.image, (self.x, self.y))


class Piston(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/piston.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.mc_default = 250
        self.move_count = self.mc_default
        self.vel = 1.5
        self.tail = [Tail(self.x + self.width // 2 - 12, self.y)]
        self.mask = pygame.mask.from_surface(self.image)

    def show_and_move(self, player):
        neg = 1
        if not player.dying:
            if self.move_count >= self.mc_default // 2:
                neg = -1
            elif self.move_count <= self.mc_default // 2:
                neg = 1
            if self.move_count == 0:
                self.move_count = self.mc_default

            self.move_count -= 1
            self.y -= self.vel * neg

        self.show_tail(neg)

        win.blit(self.image, (self.x, self.y))

    def show_tail(self, neg):
        for tail in self.tail:
            tail.show_tail()

        if self.y - (self.tail[-1].y + self.tail[-1].height) > -5 and neg == -1:
            self.tail.append(Tail(self.tail[-1].x, self.tail[-1].y + self.tail[-1].height))
        elif self.y - self.tail[-1].y < -5 and neg == 1:
            self.tail.pop(-1)
