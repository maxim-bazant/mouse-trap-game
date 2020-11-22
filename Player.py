from settings import *
import pygame


class Player(object):
    def __init__(self):
        self.x = 1500
        self.y = 100
        self.vx = 4
        self.vy = 0
        self.left_images = list()
        self.right_images = list()
        self.run_count = 0
        self.right = False
        self.left = True

        for i in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"images/mouse/left/{i}.png").convert_alpha())
        for i in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.right_images.append(pygame.image.load(f"images/mouse/right/{i}.png").convert_alpha())

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.left = False
            self.right = True

            self.x += self.vx
            if self.run_count + 1 < 4 * len(self.right_images):
                self.run_count += 1
            else:
                self.run_count = 0

            win.blit(self.right_images[self.run_count // 4], (self.x, self.y))

        elif keys[pygame.K_a]:
            self.left = True
            self.right = False

            self.x -= self.vx
            if self.run_count + 1 < 4 * len(self.left_images):
                self.run_count += 1
            else:
                self.run_count = 0

            win.blit(self.left_images[self.run_count // 4], (self.x, self.y))

        else:
            if self.right:
                win.blit(self.right_images[0], (self.x, self.y))

            elif self.left:
                win.blit(self.left_images[0], (self.x, self.y))
