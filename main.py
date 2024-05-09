import pygame
from pygame.locals import *
import random

pygame.init()
window_width = 400
window_height =400
pygame.display.set_caption("flappy bird game")
window=pygame.display.set_mode((window_width,window_height))
is_game_running=True
while is_game_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_game_running=False
pygame.quit()