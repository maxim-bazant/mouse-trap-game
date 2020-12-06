import pygame

from Collision import *
from Player import Player
from Platform import Platform
from settings import *


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.win_width = win_width
        self.win_height = win_height
        self.win = win
        self.player = Player()
        self.top_red_floor = Platform(pygame.image.load("images/floor/red_floor_5.png"),
                                      win_width, self.player.y + self.player.height)

        self.floor = [Platform(pygame.image.load("images/floor/red_floor_5.png"), win_width,
                               self.player.y + self.player.height),
                      Platform(pygame.image.load("images/floor/top_yellow_floor.png"), win_width - 320,
                               self.player.y + self.player.height),
                      Platform(pygame.image.load("images/floor/red_floor_1.png"), 128, win_height - 128),
                      Platform(pygame.image.load("images/floor/red_floor_2.png"), 128, win_height - 64),
                      Platform(pygame.image.load("images/floor/red_floor_8.png"), 128 + 512 + 64, win_height - 64),
                      Platform(pygame.image.load("images/floor/red_floor_8.png"), 128 + 512 + 64, win_height - 192),
                      Platform(pygame.image.load("images/floor/red_floor_7.png"), 128 + 512 + 64, win_height - 128),
                      Platform(pygame.image.load("images/floor/red_floor_4.png"), win_width,
                               win_height - 64)]

        self.wall = [Platform(pygame.image.load("images/floor/golden_blocks.png"),
                              self.floor[1].x - self.floor[1].width, self.player.y + self.player.height - 35),
                     Platform(pygame.image.load("images/floor/stone_wall_3.png"), self.floor[1].x - self.floor[1].width,
                              win_height - 192),
                     Platform(pygame.image.load("images/floor/stone_wall_2.png"), self.floor[5].x + 64, win_height - 128)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.player.can_not_jump = False
        self.handle_events()

        for floor in self.floor:
            floor.blit()

        for floor in self.floor:
            if floor_collision(self.player, floor):
                self.player.can_not_jump = True

        for wall in self.wall:
            wall.blit()

        for wall in self.wall:
            if wall_collision(self.player, wall):
                self.player.can_not_jump = True

        # bugging into wall bug done
        if self.player.falling_down_from_wall and self.player.falling:
            if self.player.facing_left:
                self.player.fall_left = True
            elif self.player.facing_right:
                self.player.fall_right = True

        if self.player.fall_left:
            if self.player.move_done < 16:
                self.player.x -= self.player.vel
                self.player.move_done += 1
                self.player.can_walk_right = False
            if self.player.move_done == 16:
                self.player.falling_down_from_wall = False
                self.player.move_done = 0
                self.player.fall_left = False
        if self.player.fall_right:
            if self.player.move_done < 16:
                self.player.x += self.player.vel
                self.player.move_done += 1
                self.player.can_walk_left = False
            if self.player.move_done == 16:
                self.player.falling_down_from_wall = False
                self.player.move_done = 0
                self.player.fall_right = False
        #

        keys = pygame.key.get_pressed()

        self.gravity()

        if not self.player.falling:
            self.player_movement(keys)
            if (self.player.reducing_y and self.player.can_not_jump) or self.player.no_jump_up:
                self.player.reducing_y = False
                self.player.jump_count = 4.5
                self.player.jumping = False
                self.player.walking = True
            else:
                self.player_jump(keys)
        else:
            if keys[pygame.K_LEFT] and self.player.x > 0 and self.player.can_walk_left:
                self.player.move_left()
                self.player.blit_standing()
            elif keys[pygame.K_RIGHT] and self.player.x + self.player.width < win_width and self.player.can_walk_right:
                self.player.move_right()
                self.player.blit_standing()

        if not self.player.walking or not self.player.jumping:
            self.player.blit_standing()
            self.player.walking = False

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] and not self.player.walking:
            if self.player.can_walk_left and self.player.x > 0 and self.player.can_walk_left:
                self.player.move_left()
            self.player.walking = True
            self.player.blit_moving_left()
        if keys[pygame.K_RIGHT] and not self.player.walking:
            if self.player.can_walk_right and self.player.x + self.player.width < win_width:
                self.player.move_right()
            self.player.walking = True
            self.player.blit_moving_right()

    def player_jump(self, keys):
        if keys[pygame.K_RCTRL] or self.player.jumping:
            self.player.jump()

        if keys[pygame.K_LEFT] and self.player.jumping and self.player.x > 0 and self.player.can_walk_left:
            self.player.move_left()
            self.player.blit_standing()

        if keys[pygame.K_RIGHT] and self.player.jumping and self.player.x + self.player.width < win_width \
                and self.player.can_walk_right:
            self.player.move_right()
            self.player.blit_standing()

    def gravity(self):
        if not self.player.jumping and not self.player.can_not_jump:
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
