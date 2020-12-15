from settings import *


class Flower(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/flower.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)

    def show_me(self):
        win.blit(self.image, (self.x, self.y))
