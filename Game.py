import pygame
from Player import *

# VARIABLES
win_width = 1600
win_height = 1100

win = pygame.display.set_mode((win_width, win_height))

clock = pygame.time.Clock()
FPS = 60

running = True

# MAIN LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        print("left")
    if keys[pygame.K_RIGHT]:
        print("right")
    if keys[pygame.K_RCTRL]:
        print("jumping")






