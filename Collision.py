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


def wall_collision(player, wall):  # can not go vertically or horizontally
    #  only x collision (only horizontal collision)
    if wall.y < player.y + player.height and not player.y > wall.y + wall.height:
        if player.facing_left:
            player.can_walk_right = True
            if wall.x - wall.width < player.x < wall.x:
                player.can_walk_left = False

        if player.facing_right:
            player.can_walk_left = True
            if wall.x - wall.width < player.x + player.width < wall.x:
                player.can_walk_right = False
    else:
        player.can_walk_right = True
        player.can_walk_left = True

    # y collision same code as floor_collision which is used for vertical collision only
    if abs((player.y + player.height) - wall.y) < 5:
        if player.facing_left:
            if player.x + 10 < wall.x and player.x + player.width // 2 + 5 > wall.x - wall.width:
                player.y += abs((player.y + player.height) - wall.y)
                return True
            else:
                return False

        if player.facing_right:
            if player.x + player.width - 10 < wall.x + wall.width and player.x - 5 + player.width > wall.x - wall.width:
                player.y += abs((player.y + player.height) - wall.y)
                return True
            else:
                return False

    if abs(player.y - wall.y - wall.height) < 5 and not player.falling:
        player.y -= player.y - wall.y - wall.height
        player.no_jump_up = True
    else:
        player.no_jump_up = False




















