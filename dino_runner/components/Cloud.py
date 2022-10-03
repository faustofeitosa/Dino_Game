import random

import pygame
from dino_runner.utils.constants import CLOUDS, SCREEN_WIDTH
from pygame.sprite import Sprite


class CloudManager:
    def __init__(self):
        self.clouds = []

    def update(self, game):
        if len(self.clouds) == 0:
            self.clouds.append(Cloud())
        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)

    def reset_cloud(self):
        self.clouds = []

    def draw(self, screen: pygame.Surface):
        for cloud in self.clouds:
            cloud.draw(screen)


class Cloud(Sprite):

    X_POS = SCREEN_WIDTH
    SPEEDS = (1, 1.15, 1.3, 1.35, 1.50)

    def __init__(self):
        self.speed = random.randint(0, len(self.SPEEDS) - 1)
        self.image = CLOUDS
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = 0

    def update(self, game_speed, cloud):
        acceleration = game_speed * self.SPEEDS[self.speed]
        self.rect.x -= acceleration

        if self.rect.x < -self.rect.width:
            cloud.pop()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
