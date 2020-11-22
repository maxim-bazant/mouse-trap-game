from settings import *
from Player import *
import pygame


class Game(object):
    def __init__(self):
        self.player = Player()
        self.running = True

    def new(self):
        # will show start screen
        self.run()

    def run(self):
        # will run game
        self.player.move()

    def game_over_screen(self):
        # will show game over screen
        pass


g = Game()
keys = pygame.key.get_pressed()

while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False

    win.fill((255, 255, 255))

    g.new()

    clock.tick(FPS)
    pygame.display.update()
