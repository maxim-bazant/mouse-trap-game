from settings import *


class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/ball.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.mask = pygame.mask.from_surface(self.image)
        """self.mc_default = 192
        self.move_count = self.mc_default"""  # moving

    def show_and_move(self):
        """neg = 1
        if self.move_count >= self.mc_default // 2:
            neg = -1
        elif self.move_count <= self.mc_default // 2:
            neg = 1
        if self.move_count == 0:
            self.move_count = self.mc_default

        self.move_count -= 1
        self.y -= 0.5 * neg"""  # moving the ball up and down

        win.blit(self.image, (self.x, self.y))
