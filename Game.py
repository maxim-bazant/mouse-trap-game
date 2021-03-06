import pygame

from Collision import *
from Player import Player
from Platform import Platform
from Ball import Ball
from Flower import Flower
from FallingFloor import FallingFloor
from Piston import Piston
from Door import Door
from Ladder import Ladder
from ScoreNumbers import ScoreNumbers
from FloatingText import FloatingText
from Life import Life
from Bomb import Bomb
from settings import *


class Game:
    def __init__(self):
        self.score = 0
        self.score_count = -1
        self.running = True
        self.clock = pygame.time.Clock()
        self.win_width = win_width
        self.win_height = win_height
        self.win = win
        self.play_jump_sound = True
        self.player = Player()

        self.flower = Flower(win_width // 2 - 75, self.player.y + self.player.height - 55)

        self.ceiling = pygame.image.load("images/ceiling.png")
        self.line = pygame.image.load("images/line.png")

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
                      Ball(self.wall[1].x + 5, self.floor[6].y), Ball(win_width - 64, self.floor[5].y - 64)]

        self.falling_floor = [FallingFloor(0, self.wall[0].y + 60), FallingFloor(0 + 64, self.wall[0].y + 60),

                              FallingFloor(0, self.wall[0].y + 150), FallingFloor(0 + 64, self.wall[0].y + 150),

                              FallingFloor(0, self.wall[0].y + 240), FallingFloor(0 + 64, self.wall[0].y + 240),
                              FallingFloor(0 + 64 + 64, self.wall[0].y + 240),

                              FallingFloor(0, self.wall[1].y + 5), FallingFloor(0 + 64, self.wall[1].y + 5),

                              FallingFloor(0, self.floor[2].y + 5)]

        self.pistons = [Piston(self.floor[1].x - self.floor[1].width, self.floor[1].y + self.floor[1].height + 180, 9),
                        Piston(self.floor[1].x - self.floor[1].width + 125, self.floor[1].y + self.floor[1].height + 120, 7),
                        Piston(self.floor[1].x - self.floor[1].width + 250, self.floor[1].y + self.floor[1].height + 60, 4),
                        Piston(self.floor[1].x - self.floor[1].width + 375, self.floor[1].y + self.floor[1].height + 0, 1)]

        self.ladder = [Ladder(self.wall[2].x + self.wall[2].width, self.floor[7].y - 64),
                       Ladder(self.wall[2].x + self.wall[2].width, self.floor[7].y - 64 * 2),
                       Ladder(self.wall[2].x + self.wall[2].width, self.floor[7].y - 64 * 3),
                       Ladder(self.wall[2].x + self.wall[2].width, self.floor[7].y - 64 * 4),

                       Ladder(self.wall[2].x, self.floor[7].y - 64 * 4 - 32),
                       Ladder(self.wall[2].x + self.wall[2].width * 2 - 5, self.floor[7].y - 64 * 4 - 32)]

        # floor next to the ladder
        self.floor.append(Platform(pygame.image.load("images/floor/red_floor_1.png"),
                                   self.ladder[-2].x + self.ladder[-2].width, self.ladder[-2].y + 64))
        self.floor.append(Platform(pygame.image.load("images/floor/red_floor_1.png"),
                                   self.ladder[-1].x + self.ladder[-1].width - 5, self.ladder[-1].y + 64))

        self.door = Door(self.wall[2].x + self.wall[2].width, self.ladder[-1].y - 64 - 48 - 5)

        # floor under door
        self.floor.append(Platform(pygame.image.load("images/floor/red_floor_3.png"),
                                   self.door.x + 64 * 2 - 5, self.door.y + self.door.height - 16))

        self.congrats = pygame.image.load("images/text/congrats.png")
        self.you_lost = pygame.image.load("images/text/you_lost.png")

        self.score_numbers = [ScoreNumbers(self.wall[2].x - 128, win_height - 64),
                              ScoreNumbers(self.wall[2].x - 192, win_height - 64),
                              ScoreNumbers(self.wall[2].x - 256, win_height - 64),
                              ScoreNumbers(self.wall[2].x - 320, win_height - 64),
                              ScoreNumbers(self.wall[2].x - 384, win_height - 64),
                              ScoreNumbers(self.wall[2].x - 448, win_height - 64)]

        self.mouse_trap_text = [FloatingText(750, 200, False, 15, True),
                                FloatingText(150, 500, True, 15, True),
                                FloatingText(win_width + 20, 20, False, 5, False)]

        self.lives_images = [Life(win_width + 20, 130),
                             Life(win_width + 20, 230),
                             Life(win_width + 20, 320),
                             Life(win_width + 20, 410)]

        self.bomb = Bomb(win_width + 150, win_height - 125)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def level_done_screen(self):
        win.fill(bg_color)
        win.blit(self.congrats, (30 + side_width // 2, win_height // 2 - 50))
        self.clock.tick(FPS)
        pygame.display.update()

        time.sleep(2)

    def game_over_screen(self):
        win.fill(bg_color)
        win.blit(self.you_lost, (30 + side_width // 2, win_height // 2 - 50))
        self.clock.tick(FPS)
        pygame.display.update()

        time.sleep(2)

    def game(self):
        self.blit_and_init()

        self.collision()

        if not self.player.dying and not self.player.going_into_door and self.player.lives != 0:
            # player movement

            if self.player.move_left_bc_tha_wall:
                self.player.can_walk_right = False
                self.player.can_walk_left = False
                self.player.x -= self.player.vel + 1.5
            if self.player.move_right_bc_tha_wall:
                self.player.x += self.player.vel + 1.5
                self.player.can_walk_left = False
                self.player.can_walk_right = False

            keys = pygame.key.get_pressed()

            self.gravity()
            self.fall_damage()

            if not self.player.falling:
                self.player_movement(keys)
                if (self.player.reducing_y and self.player.can_not_jump) or self.player.no_jump_up:
                    self.play_jump_sound = True
                    self.player.reducing_y = False
                    self.player.jump_count = 4.5
                    self.player.jumping = False
                    self.player.walking = True
                else:
                    self.player_jump(keys)
            else:
                if keys[pygame.K_LEFT] and self.player.x > 0 and self.player.can_walk_left and self.player.facing_left:
                    self.player.move_left()
                    self.player.blit_standing()
                elif keys[pygame.K_RIGHT] and self.player.x + self.player.width < win_width and \
                        self.player.can_walk_right and self.player.facing_right:
                    self.player.move_right()
                    self.player.blit_standing()

            if not self.player.walking or not self.player.jumping:
                self.player.blit_standing()
                self.player.walking = False

        elif self.player.dying:
            self.player.blit_dying()
            if self.player.done_dying:
                self.reset_setup()

        elif self.player.going_into_door:
            self.door.mouse_going_into_door()
            if self.door.mouse_done_going_into_door:

                self.level_done_screen()

                self.reset_setup()
                self.player.reset()
                self.door.mouse_done_going_into_door = False
                self.score = 0

        elif self.player.lives == 0:
            self.score = 0
            self.game_over_screen()

            self.reset_setup()
            self.player.reset()

    def reset_setup(self):
        self.balls = [Ball(win_width // 2 - 75, 50), Ball(0, self.wall[0].y + self.wall[0].y // 2 - 15),
                      Ball(64, self.wall[1].y - 64),
                      Ball(self.wall[1].x + 5, self.floor[6].y), Ball(win_width - 64, self.floor[5].y - 64)]
        self.pistons = [Piston(self.floor[1].x - self.floor[1].width, self.floor[1].y + self.floor[1].height + 180, 9),
                        Piston(self.floor[1].x - self.floor[1].width + 125, self.floor[1].y + self.floor[1].height + 120, 7),
                        Piston(self.floor[1].x - self.floor[1].width + 250, self.floor[1].y + self.floor[1].height + 60, 4),
                        Piston(self.floor[1].x - self.floor[1].width + 375, self.floor[1].y + self.floor[1].height + 0, 1)]

        self.falling_floor = [FallingFloor(0, self.wall[0].y + 60 + 2),
                              FallingFloor(0 + 64, self.wall[0].y + 60 + 2),

                              FallingFloor(0, self.wall[0].y + 150 + 2),
                              FallingFloor(0 + 64, self.wall[0].y + 150 + 2),

                              FallingFloor(0, self.wall[0].y + 240 + 2),
                              FallingFloor(0 + 64, self.wall[0].y + 240 + 2),
                              FallingFloor(0 + 64 + 64, self.wall[0].y + 240 + 2),

                              FallingFloor(0, self.wall[1].y + 5), FallingFloor(0 + 64, self.wall[1].y + 5),

                              FallingFloor(0, self.floor[2].y + 5)]

        self.bomb = Bomb(win_width + 150, win_height - 125)
        self.play_jump_sound = True

    def collision(self):
        for falling_floor in self.falling_floor:
            if falling_floor_collision(self.player, falling_floor):
                self.player.can_not_jump = True
                if falling_floor.fall_count <= 70 and not self.player.dying:
                    falling_floor.fall()
                elif falling_floor.fall_count > 70:
                    self.falling_floor.remove(falling_floor)

        for ladder in self.ladder:
            if ladder_collision(self.player, ladder):
                self.player.can_not_jump = True

        for floor in self.floor:
            if floor == self.floor[1]:
                number = 10
            elif floor == self.floor[-1]:
                number = 4
            else:
                number = 5

            if floor_collision(self.player, floor, number):
                self.player.can_not_jump = True

        for wall in self.wall:
            if wall_collision(self.player, wall) == 1:
                self.player.can_walk_left = False
            elif wall_collision(self.player, wall) == 2:
                self.player.can_walk_right = False
            elif wall_collision(self.player, wall) == 3:
                self.player.can_not_jump = True
            elif wall_collision(self.player, wall) == 4:
                self.player.no_jump_up = True

        for ball in self.balls:
            if ball_collision(self.player, ball):
                pickup_sound.play()
                self.score += 40
                self.balls.remove(ball)

        for piston in self.pistons:
            if piston_collision(self.player, piston):
                self.player.dying = True

        if flower_collision(self.player, self.flower) == 1:
            self.player.dying = True
        elif flower_collision(self.player, self.flower) == 3:
            self.player.can_not_jump = True

        if self.door.open:
            if door_collision(self.player, self.door):
                self.player.going_into_door = True

        if self.bomb.explode_:
            self.player.dying = True

    def blit_and_init(self):
        self.player.can_walk_left = True
        self.player.can_walk_right = True
        self.player.can_not_jump = False
        self.player.no_jump_up = False
        self.handle_events()

        for mouse_trap_text in self.mouse_trap_text:
            mouse_trap_text.show_and_move(self.player)

        for life in range(self.player.lives):
            self.lives_images[life].show_me()

        win.blit(self.ceiling, (0, -4))
        win.blit(self.line, (win_width, 0))

        for floor in self.floor:
            floor.show_me()

        for falling_floor in self.falling_floor:
            falling_floor.show_me()

        for wall in self.wall:
            wall.show_me()

        for ball in self.balls:
            ball.show_and_move()

        for ladder_ in self.ladder:
            ladder_.show_me()

        for piston in self.pistons:
            piston.show_and_move(self.player)

        for score_ in self.score_numbers:
            if self.score_count < len(self.score_numbers) - 1:
                self.score_count += 1
            else:
                self.score_count = 0

            score_list = list(str(self.score))
            score_list.reverse()

            try:
                score_.show_me(int(score_list[self.score_count]))
            except IndexError:
                score_.show_me(0)

        if not self.player.going_into_door:
            self.door.show_me(self.balls)

        self.bomb.show_me()

        self.flower.show_me()

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] and not self.player.walking and not self.player.jumping and not self.player.falling:
            if self.player.can_walk_left and self.player.x > 0 and self.player.can_walk_left:
                self.player.move_left()
            self.player.walking = True
            self.player.blit_moving_left()
        if keys[pygame.K_RIGHT] and not self.player.walking and not self.player.jumping and not self.player.falling:
            if self.player.can_walk_right and self.player.x + self.player.width < win_width:
                self.player.move_right()
            self.player.walking = True
            self.player.blit_moving_right()
        else:
            self.player.blit_standing()

    def player_jump(self, keys):
        if keys[pygame.K_SPACE] or self.player.jumping:
            if self.play_jump_sound:
                jump_sound.play()
                self.play_jump_sound = False

            if self.player.walking:
                if self.player.facing_left:
                    self.player.jump(self.play_jump_sound)
                    if self.player.jumping and self.player.x > 0 and self.player.can_walk_left:
                        self.player.x -= self.player.jumping_vel

                elif self.player.facing_right:
                    self.player.jump(self.play_jump_sound)
                    if self.player.jumping and self.player.x + self.player.width < win_width\
                            and self.player.can_walk_right:
                        self.player.x += self.player.jumping_vel
            else:
                self.player.jump(self.play_jump_sound)

    def fall_damage(self):
        if self.player.reducing_y or self.player.falling:
            self.player.fall_damage_count += 1
            if self.player.fall_damage_count > 50:
                self.player.die_bc_fall_damage = True
        else:
            self.player.fall_damage_count = 0
            if self.player.die_bc_fall_damage:
                self.player.dying = True

    def gravity(self):
        if not self.player.jumping and not self.player.can_not_jump and not self.player.y > win_height - 160:
            self.player.falling = True
            self.player.y += self.player.acc
        else:
            self.player.falling = False

        if self.player.y > win_height - 160:
            self.player.y = win_height - 160

    def run(self):
        self.game()


g = Game()

# MAIN LOOP
while g.running:
    g.win.fill(bg_color)

    g.run()

    g.clock.tick(FPS)
    pygame.display.update()
