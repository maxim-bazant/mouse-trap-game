import pygame
from Player import *
from Platform import *
from settings import *


def floor_collision(player, floor):  # can go through vertically but not horizontally
    if abs((player.y + player.height) - floor.y) < 5:
        if player.facing_left:
            if player.x + player.width // 2 + 10 > floor.x - floor.width and player.x < floor.x:
                player.y += abs((player.y + player.height) - floor.y)
                return True
            else:
                return False
        elif player.facing_right:
            if player.x + player.width > floor.x - floor.width and player.x + player.width / 2 - 10 < floor.x:
                player.y += abs((player.y + player.height) - floor.y)
                return True
            else:
                return False


def wall_collision(player, wall):  # can not go vertically or horizontally
    if player.y + player.height > wall.y and not player.y > wall.y + wall.height:
        if player.facing_left:
            if player.x < wall.x and not player.x + player.width // 2 - 10 < wall.x:
                return 0  # 0 for not able to walk left
        if player.facing_right:
            if player.x + player.width // 2 - 10 > wall.x - wall.width * 2 and\
               not player.x + player.width // 2 + 10 > wall.x:
                return 1  # 1 for not able to walk right

    if abs((player.y + player.height) - wall.y) < 5:
        if player.facing_left:
            if player.x + 10 < wall.x and player.x + player.width // 2 > wall.x - wall.width:
                player.y += abs((player.y + player.height) - wall.y)
                return 3

        if player.facing_right:
            if player.x + player.width + 10 > wall.x - wall.width and \
               player.x - player.width // 2 - 20 < wall.x - wall.width * 2:
                player.y += abs((player.y + player.height) - wall.y)
                return 3

    if abs(wall.y + wall.height - player.y) < 6 and not player.falling:
        if player.facing_left:
            if player.x + 10 < wall.x and player.x + player.width // 2 > wall.x - wall.width:
                return 4

        if player.facing_right:
            if player.x + player.width + 10 > wall.x - wall.width and \
                    player.x - player.width // 2 - 10 < wall.x - wall.width * 2:
                return 4






















