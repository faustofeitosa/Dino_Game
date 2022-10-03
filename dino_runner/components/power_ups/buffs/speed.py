import random

import pygame
from dino_runner.utils.constants import CLOCK


class Speed:
    def __init__(self, axle_y, axle_x):
        self.image = CLOCK
        self.rect = self.image.get_rect()
        self.rect.y = axle_y
        self.rect.x = axle_x

    def update(self, game, manager):
        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            manager.power_ups.pop()

    def activate(self, game, manager=""):
        game.game_speed -= 10

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
