import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, image, type):
        # Cactus
        self.type = type
        self.image = image[self.type]
        # DinoFlying
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacle: list):

        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacle.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
