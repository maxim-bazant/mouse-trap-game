import pygame

from Collision import *
from Player import Player
from Platform import Platform
from Ball import Ball
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
                     Platform(pygame.image.load("images/floor/stone_wall_2.png"), self.floor[5].x + 64,
                              win_height - 128)]

        self.balls = [Ball(win_width // 2 - 75, 50), Ball(0, self.wall[0].y + self.wall[0].y // 2 - 15),
                      Ball(64, self.wall[1].y - 64),
                      Ball(self.wall[1].x, self.floor[6].y), Ball(win_width - 64, self.floor[5].y - 64)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.blit_and_init()

        for wall in self.wall:
            if wall_collision(self.player, wall) == 1:
                self.player.can_walk_left = False
            elif wall_collision(self.player, wall) == 2:
                self.player.can_walk_right = False
            elif wall_collision(self.player, wall) == 3:
                self.player.can_not_jump = True
            elif wall_collision(self.player, wall) == 4:
                self.player.no_jump_up = True

        if self.player.move_left_bc_tha_wall:
            self.player.can_walk_right = False
            self.player.x -= self.player.vel - 0.4
        elif self.player.move_right_bc_tha_wall:
            self.player.x += self.player.vel - 0.4
            self.player.can_walk_left = False

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

    def blit_and_init(self):
        self.player.can_walk_left = True
        self.player.can_walk_right = True
        self.player.can_not_jump = False
        self.player.no_jump_up = False
        self.handle_events()

        for floor in self.floor:
            floor.blit()

        for floor in self.floor:
            if floor_collision(self.player, floor):
                self.player.can_not_jump = True

        for wall in self.wall:
            wall.blit()

        for ball in self.balls:
            ball.show_and_move()

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] and not self.player.walking and not self.player.jumping:
            if self.player.can_walk_left and self.player.x > 0 and self.player.can_walk_left:
                self.player.move_left()
            self.player.walking = True
            self.player.blit_moving_left()
        if keys[pygame.K_RIGHT] and not self.player.walking and not self.player.jumping:
            if self.player.can_walk_right and self.player.x + self.player.width < win_width:
                self.player.move_right()
            self.player.walking = True
            self.player.blit_moving_right()

    def player_jump(self, keys):
        if keys[pygame.K_SPACE] or self.player.jumping:
            if self.player.walking:
                if self.player.facing_left:
                    self.player.jump()
                    if self.player.jumping and self.player.x > 0 and self.player.can_walk_left:
                        self.player.x -= self.player.jumping_vel

                elif self.player.facing_right:
                    self.player.jump()
                    if self.player.jumping and self.player.x + self.player.width < win_width\
                            and self.player.can_walk_right:
                        self.player.x += self.player.jumping_vel
            else:
                self.player.jump()
            self.player.blit_standing()

    def gravity(self):
        if not self.player.jumping and not self.player.can_not_jump and not self.player.y > win_height - 160:
            self.player.falling = True
            self.player.y += self.player.acc
        else:
            self.player.falling = False

        if self.player.y > win_height - 160:
            self.player.y = win_height - 160

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
