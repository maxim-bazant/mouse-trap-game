import pygame

from Player import Player
from settings import *


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.win_width = win_width
        self.win_height = win_height
        self.win = win
        self.player = Player()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.handle_events()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and not self.player.walking:
            self.player.move_left()
            self.player.walking = True
        if keys[pygame.K_RIGHT] and not self.player.walking:
            self.player.move_right()
            self.player.walking = True
        if keys[pygame.K_RCTRL] or self.player.jumping:
            self.player.jump()
        else:
            self.player.stand()
            self.player.walking = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.start_screen()
        self.game()
        self.game_over_screen()


g = Game()

# MAIN LOOP
while g.running:
    g.win.fill(bg_color)

    g.run()

    g.clock.tick(FPS)
    pygame.display.update()






