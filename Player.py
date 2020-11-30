import pygame


class Player:
    def __init__(self):
        self.x = Game().win_width - self.width
        self.y = 200

        self.right_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"mouse/right/{number}.png"))

        self.left_images = []
        for number in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"mouse/left/{number}.png"))

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height
        self.vel = 5
        self.moving_left = True
        self.moving_right = False

    def move_right(self):
        self.moving_right = True
        self.x += self.vel
        self.blit_me()

    def move_left(self):
        self.moving_right = True
        self.x -= self.vel
        self.blit_me()

    def jump(self):
        pass

    def blit_me(self):
        if self.moving_right:
            pass
        elif self.moving_left:
            pass
