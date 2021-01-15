from settings import *
import pygame


class FloatingText(object):
    def __init__(self, x, y, go_down, image_changer, move):
        self.x = x
        self.y = y
        self.go_down = go_down  # True = down, False = up
        self.move = move
        self.vel = 1

        self.images = []
        for number in ["01", "02"]:
            self.images.append(pygame.image.load(f"images/text/mouse_trap_text_{number}.png").convert_alpha())

        self.width = self.images[0].get_rect().width
        self.height = self.images[1].get_rect().height
        self.show_count = 0
        self.image_changer = image_changer

    def show_and_move(self, player):
        if self.show_count + 1 < len(self.images) * self.image_changer:
            self.show_count += 1
        else:
            self.show_count = 0

        win.blit(self.images[self.show_count // self.image_changer], (self.x, self.y))

        # move
        if not player.dying:
            if self.move:
                if self.go_down:
                    if self.y < win_height:
                        self.y += self.vel
                    else:
                        self.y = -85

                elif not self.go_down:
                    if self.y > -85:
                        self.y -= self.vel
                    else:
                        self.y = win_height

