import pygame
from pygame.locals import *
import random

pygame.init()
window_width = 864
window_height = 800
# got from someone GitHub
background = pygame.image.load("bg.png")
pygame.display.set_caption("flappy bird game")
window = pygame.display.set_mode((window_width, window_height))
is_game_running = True
while is_game_running:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        # to check if quit pressed
        if event.type == pygame.QUIT:
            is_game_running = False
    pygame.display.update()
pygame.quit()
