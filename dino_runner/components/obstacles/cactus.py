import random

import pygame
from dino_runner.utils.constants import (LARGE_CACTUS, SCREEN_WIDTH,
                                         SMALL_CACTUS)


class Cactus():
    X_POS = SCREEN_WIDTH
    CACTUS = {
        "LARGE": (LARGE_CACTUS, 300),
        "SMALL": (SMALL_CACTUS, 323),
    }

    def __init__(self, cactus_type):
        self.image, self.Y_POS = self.CACTUS[cactus_type]
        self.type = random.randint(0, 2)
        self.rect = self.image[self.type].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS

    def update(self, game_speed, obstacle):
        self.rect.y = self.Y_POS

        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacle.pop()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image[self.type], self.rect)
