from Player import Player
import pygame


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.win_width = 1600
        self.win_height = 1100
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.FPS = 60
        self.player = Player()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass

    def game(self):
        self.handle_events()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_RCTRL]:
            self.player.jump()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.start_screen()
        self.game()
        self.game_over_screen()


g = Game()

# MAIN LOOP
while g.running:
    g.run()






