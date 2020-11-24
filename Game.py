from settings import *
from Floor import *
from Player import *
import pygame


class Game(object):
    def __init__(self):
        self.player = Player()
        self.running = True
        self.top_red_floor = []
        for tile in range(5):
            if not self.top_red_floor:
                self.top_red_floor.append(RedFloorTile(win_width - 68, 500))
            else:
                self.top_red_floor.append(RedFloorTile(self.top_red_floor[-1].x - self.top_red_floor[-1].width, 500))

    def new(self):
        # will show start screen
        self.run()

    def run(self):
        # will run game
        self.player.movement()
        for tile in self.top_red_floor:
            tile.show()

    def game_over_screen(self):
        # will show game over screen
        pass


g = Game()
keys = pygame.key.get_pressed()

while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False

    win.fill((0, 120, 130))

    g.new()

    clock.tick(FPS)
    pygame.display.update()
