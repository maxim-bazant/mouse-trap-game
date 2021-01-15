import pygame

win_width = 1021
win_height = 780
side_width = 250
FPS = 100
win = pygame.display.set_mode((win_width + side_width, win_height))

bg_color = (0, 120, 130)  # color most similar to original bg color

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.font.init()
pygame.init()

bg_music = pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 means that it will play the music infinitely

jump_sound = pygame.mixer.Sound("sound/jump.wav")
pickup_sound = pygame.mixer.Sound("sound/pickup_coin_sound.wav")
dying_sound = pygame.mixer.Sound("sound/death_sound.wav")
dying_sound.set_volume(0.15)
