import random

import pygame
from dino_runner.utils.constants import HEARTH_STATUS


class Life:
    def __init__(self, axle_y, axle_x):
        self.image = HEARTH_STATUS[0]
        self.rect = self.image.get_rect()
        self.rect.y = axle_y
        self.rect.x = axle_x

    def update(self, game, manager):
        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            manager.power_ups.pop()

    def activate(self, game, manager=""):
        if not game.life_count == 3:
            game.life_count += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
