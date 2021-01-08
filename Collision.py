import pygame
from Player import *
from Platform import *
from settings import *

space_right = 5
space_left = 5


def floor_collision(player, floor, number):  # can go through vertically but not horizontally
    if abs((player.y + player.height) - floor.y) < number and player.y + player.height - 2 < floor.y:
        if player.facing_left:
            if player.x + player.width // 2 + space_left > floor.x - floor.width and player.x < floor.x:
                player.y += abs((player.y + player.height) - floor.y)
                return True
            else:
                return False
        elif player.facing_right:
            if player.x + player.width > floor.x - floor.width and player.x + player.width / 2 - space_right < floor.x:
                player.y += abs((player.y + player.height) - floor.y)
                return True
            else:
                return False


def falling_floor_collision(player, falling_floor):
    if abs((player.y + player.height) - falling_floor.y) < 5:
        if player.facing_left:
            if player.x < falling_floor.x + falling_floor.width and player.x + player.width // 2 > falling_floor.x:
                player.y += abs((player.y + player.height) - falling_floor.y)
                return True
            else:
                return False
        elif player.facing_right:
            if player.x + player.width - space_right > falling_floor.x and \
                    player.x + player.width // 2 < falling_floor.x + falling_floor.width:
                player.y += abs((player.y + player.height) - falling_floor.y)
                return True
            else:
                return False


def ladder_collision(player, ladder):
    if abs((player.y + player.height) - ladder.y) < 5:
        if player.facing_left:
            if player.x < ladder.x + ladder.width and player.x + player.width // 2 + space_right > ladder.x:
                player.y += abs((player.y + player.height) - ladder.y)
                return True
            else:
                return False
        elif player.facing_right:
            if player.x + player.width > ladder.x and player.x + player.width // 2 < ladder.x + ladder.width:
                player.y += abs((player.y + player.height) - ladder.y)
                return True
            else:
                return False


def wall_collision(player, wall):  # can not go vertically or horizontally
    if player.y + player.height > wall.y and not player.y > wall.y + wall.height:
        if player.facing_left:
            if player.x < wall.x < player.x + player.width // 2 - space_left:
                return 1  # 0 for not able to walk left

            if player.x + player.width // 2 - space_right > wall.x - wall.width * 2 and\
               player.x + player.width // 2 + space_right < wall.x:
                player.move_left_bc_tha_wall = True
            else:
                player.move_left_bc_tha_wall = False

        if player.facing_right:
            if player.x + player.width // 2 - space_right > wall.x - wall.width * 2 and\
               player.x + player.width // 2 - space_right * 2 < wall.x:
                return 2  # 1 for not able to walk right

            if player.x < wall.x < player.x + player.width // 2 + space_right or 715 < player.x < 755.5:
                player.move_right_bc_tha_wall = True
            else:
                player.move_right_bc_tha_wall = False

    if abs((player.y + player.height) - wall.y) < 5:
        if player.facing_left:
            if player.x + space_left < wall.x and player.x + player.width // 2 > wall.x - wall.width:
                player.y += abs((player.y + player.height) - wall.y)
                return 3

        if player.facing_right:
            if player.x + player.width - space_right * 2 > wall.x - wall.width and \
               player.x - player.width // 2 - space_right * 4 < wall.x - wall.width * 2:
                player.y += abs((player.y + player.height) - wall.y)
                return 3

    if abs(wall.y + wall.height - player.y) < 10:
        if player.facing_left:
            if player.x < wall.x and player.x + player.width // 2 > wall.x - wall.width:
                return 4

        if player.facing_right:
            if player.x + player.width > wall.x - wall.width and \
                    player.x - player.width // 2 < wall.x - wall.width * 2:
                return 4


def ball_collision(player, ball):
    offset = (int(player.x - ball.x), int(player.y - ball.y))
    collision = ball.mask.overlap(player.mask, offset)
    if collision:
        return True


def flower_collision(player, flower):
    if player.y + player.height > flower.y and not player.y > flower.y + flower.height:  # means player is below flower
        if player.facing_left:
            if player.x < flower.x + flower.width and player.x + player.width // 2 - space_left > flower.x:
                return 1

            if flower.x < player.x + player.width < flower.x + flower.width:
                player.move_left_bc_tha_wall = True
            else:
                if not player.move_left_bc_tha_wall:
                    player.move_left_bc_tha_wall = False

        if player.facing_right:
            if flower.x < player.x + player.width < flower.x + flower.width:
                return 1

            if player.x < flower.x + flower.width and player.x + player.width // 2 - space_left > flower.x:
                player.move_right_bc_tha_wall = True
            else:
                if not player.move_right_bc_tha_wall:
                    player.move_right_bc_tha_wall = False

    elif abs((player.y + player.height) - flower.y) < 5:
        if player.facing_left:
            if player.x < flower.x + flower.width and player.x + player.width // 2 > flower.x:
                player.y += abs((player.y + player.height) - flower.y)
                return 3
        elif player.facing_right:
            if flower.x < player.x + player.width // 2 < flower.x + flower.width:
                player.y += abs((player.y + player.height) - flower.y)
                return 3


def piston_collision(player, piston):
    offset = (int(player.x - piston.x), int(player.y - piston.y))
    collision = piston.mask.overlap(player.mask, offset)
    if collision:
        return True








