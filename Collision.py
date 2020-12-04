import pygame
from Player import *
from Floor import *
from settings import *


def horizontal_collision(player, floor):
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


