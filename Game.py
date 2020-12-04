import pygame

from Collision import *
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
        self.top_red_floor = HorizontalFloor(pygame.image.load("images/floor/top_red_floor.png"),
                                             win_width, self.player.y + self.player.height)
        self.touching = False

        self.floors = [HorizontalFloor(pygame.image.load("images/floor/top_red_floor.png"), win_width,
                                       self.player.y + self.player.height),
                       HorizontalFloor(pygame.image.load("images/floor/top_yellow_floor.png"), win_width - 320,
                                       self.player.y + self.player.height)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.touching = False
        self.handle_events()

        for floor in self.floors:
            floor.blit()

        for floor in self.floors:
            if horizontal_collision(self.player, floor):
                self.touching = True

        keys = pygame.key.get_pressed()

        self.gravity()

        if not self.player.falling:
            self.player_movement(keys)
            if self.player.reducing_y and not self.touching:
                self.player.reducing_y = False
                self.player.jump_count = 4.5
                self.player.jumping = False
                self.player.walking = True
            else:

                self.player_jump(keys)
        else:
            if keys[pygame.K_LEFT] and self.player.x > 0:
                self.player.move_left()
                self.player.blit_standing()
            elif keys[pygame.K_RIGHT] and self.player.x + self.player.width < win_width:
                self.player.move_right()
                self.player.blit_standing()

        if not self.player.walking or not self.player.jumping:
            self.player.blit_standing()
            self.player.walking = False

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] and not self.player.walking and self.player.x > 0:
            self.player.move_left()
            self.player.blit_moving_left()
            self.player.walking = True
        if keys[pygame.K_RIGHT] and not self.player.walking and self.player.x + self.player.width < win_width:
            self.player.move_right()
            self.player.blit_moving_right()
            self.player.walking = True

    def player_jump(self, keys):
        if keys[pygame.K_RCTRL] or self.player.jumping:
            self.player.jump()

        if keys[pygame.K_LEFT] and self.player.jumping and self.player.x > 0:
            self.player.move_left()
            self.player.blit_standing()

        if keys[pygame.K_RIGHT] and self.player.jumping and self.player.x + self.player.width < win_width:
            self.player.move_right()
            self.player.blit_standing()

    def gravity(self):
        if self.player.y < win_height - self.player.height and not self.player.jumping \
           and not self.touching:
            self.player.falling = True
            self.player.y += self.player.acc
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
