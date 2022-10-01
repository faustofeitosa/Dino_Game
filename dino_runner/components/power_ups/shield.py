import time

import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, SHIELD


class Shield:
    Y_POS = 100
    X_POS = SCREEN_WIDTH

    def __init__(self):
        self.image = SHIELD
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.count_time = 10

    def update(self, game, manager):

        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            manager.power_ups.pop()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
