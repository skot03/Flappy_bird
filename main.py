import pygame
from pygame.locals import *
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bird1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


clock = pygame.time.Clock()
fps = 60
ground_speed = 0
speed_left = 4
pygame.init()
window_width = 800
window_height = 936
bird_group = pygame.sprite.Group()
flappy = Bird(100, int(window_height / 2))
bird_group.add(flappy)
# got from someone GitHub
background = pygame.image.load("bg.png")
ground = pygame.image.load("ground.png")
pygame.display.set_caption("flappy bird game")
window = pygame.display.set_mode((window_width, window_height))
is_game_running = True
while is_game_running:
    clock.tick(fps)
    # adding images to screen
    window.blit(background, (0, 0))
    bird_group.draw(window)
    window.blit(ground, (ground_speed, 768))
    ground_speed -= speed_left
    if abs(ground_speed) > 35:
        ground_speed = 0

    for event in pygame.event.get():
        # to check if quit pressed
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.update()
pygame.quit()
