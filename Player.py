from settings import *
import pygame


class Player(object):
    def __init__(self):
        self.x = 1500
        self.y = 100
        self.vx = 5
        self.vy = 5
        self.left_images = list()
        self.right_images = list()
        self.run_count = 0
        self.right = False
        self.left = True
        self.image_repeater = 3
        self.falling = False
        self.jumping = False
        self.jump_count = 5.25
        self.last_direction = None

        for i in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.left_images.append(pygame.image.load(f"images/mouse/left/{i}.png").convert_alpha())
        for i in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            self.right_images.append(pygame.image.load(f"images/mouse/right/{i}.png").convert_alpha())

        self.width = self.right_images[0].get_rect().width
        self.height = self.right_images[0].get_rect().height

    def move(self):
        if not self.falling:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                self.left = False
                self.right = True
                self.last_direction = "right"

                self.x += self.vx
                if self.run_count + 1 < self.image_repeater * len(self.right_images):
                    self.run_count += 1
                else:
                    self.run_count = 0

                win.blit(self.right_images[self.run_count // self.image_repeater], (self.x, self.y))

            elif keys[pygame.K_a]:
                self.left = True
                self.right = False
                self.last_direction = "left"

                self.x -= self.vx
                if self.run_count + 1 < self.image_repeater * len(self.left_images):
                    self.run_count += 1
                else:
                    self.run_count = 0

                win.blit(self.left_images[self.run_count // self.image_repeater], (self.x, self.y))

            else:
                if self.right:
                    win.blit(self.right_images[0], (self.x, self.y))

                elif self.left:
                    win.blit(self.left_images[0], (self.x, self.y))

    def jump(self):
        if not self.falling:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.jumping = True

            if self.jumping:
                if self.jump_count >= -5.25:
                    if keys[pygame.K_d]:
                        self.x += self.vx
                        win.blit(self.right_images[0], (self.x, self.y))
                    elif keys[pygame.K_a]:
                        self.x -= self.vx
                        win.blit(self.left_images[0], (self.x, self.y))
                    else:
                        if self.right:
                            win.blit(self.right_images[0], (self.x, self.y))

                        elif self.left:
                            win.blit(self.left_images[0], (self.x, self.y))

                    neg = 1
                    if self.jump_count < 0:
                        neg = -1
                    self.y -= (self.jump_count ** 2) * 0.5 * neg
                    self.jump_count -= 0.25
                else:
                    self.jump_count = 5.25
                    self.jumping = False

    def fall(self):
        if not self.touching() and self.y < win_height - self.height and not self.jumping:
            self.falling = True
            self.y += self.vy + 0.5
            self.vy += 0.1
            if self.right:
                win.blit(self.right_images[0], (self.x, self.y))

            elif self.left:
                win.blit(self.left_images[0], (self.x, self.y))

        else:
            self.falling = False

    def touching(self):  # collision
        return False

    def movement(self):
        if not self.jumping:
            self.move()
        self.jump()
        self.fall()













