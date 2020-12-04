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
            if player.x + player.width // 2 + 10 > floor.x - floor.width and player.x + player.width / 2 - 10 < floor.x:
                player.y += abs((player.y + player.height) - floor.y)
                return True
            else:
                return False


def wall_collision():  # can not go vertically or horizontally
    pass
