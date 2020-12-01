import pygame

from Player import Player
from Floor import HorizontalFloor
from settings import *


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.win_width = win_width
        self.win_height = win_height
        self.win = win
        self.player = Player()
        self.top_red_floor = HorizontalFloor(pygame.image.load("images/floor/top_red_floor.png"), win_width, 400)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.handle_events()

        self.top_red_floor.blit()

        keys = pygame.key.get_pressed()

        self.gravity()

        if not self.player.falling:
            self.player_movement(keys)
            self.player_jump(keys)

        if not self.player.walking or not self.player.jumping:
            self.player.blit_standing()
            self.player.walking = False

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] and not self.player.walking:
            self.player.move_left()
            self.player.walking = True
        if keys[pygame.K_RIGHT] and not self.player.walking:
            self.player.move_right()
            self.player.walking = True

    def player_jump(self, keys):
        if keys[pygame.K_RCTRL] or self.player.jumping:
            self.player.jump()

        if keys[pygame.K_LEFT] and self.player.jumping:
            self.player.facing_left = True
            self.player.facing_right = False
            self.player.x -= self.player.jumping_vel

        if keys[pygame.K_RIGHT] and self.player.jumping:
            self.player.facing_left = False
            self.player.facing_right = True
            self.player.x += self.player.jumping_vel

    def gravity(self):
        if self.player.y < win_height - self.player.height and not self.player.jumping:
            self.player.falling = True
            self.player.y += self.player.acc
            self.player.acc += 0.1
        else:
            self.player.falling = False

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






