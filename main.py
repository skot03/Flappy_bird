import pygame
from pygame.locals import *
import random

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for loop in range(1, 4):
            actual = pygame.image.load(f"bird{loop}.png")
            self.images.append(actual)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        # Change animation
        self.counter += 1
        flap_cooldown = 15
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

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
# Got from someone GitHub
background = pygame.image.load("bg.png")
ground = pygame.image.load("ground.png")
pygame.display.set_caption("Flappy Bird Game")
window = pygame.display.set_mode((window_width, window_height))
is_game_running = True
while is_game_running:
    clock.tick(fps)
    # Adding images to screen
    window.blit(background, (0, 0))
    bird_group.draw(window)
    bird_group.update()
    window.blit(ground, (ground_speed, 768))
    ground_speed -= speed_left
    if abs(ground_speed) > 35:
        ground_speed = 0

    for event in pygame.event.get():
        # To check if quit pressed
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.update()
pygame.quit()
