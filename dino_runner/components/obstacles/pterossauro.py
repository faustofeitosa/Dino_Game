import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class DinoFlying(Obstacle):
    Y_POS = 250
    X_POS = SCREEN_WIDTH

    def __init__(self):
        self.dino_flying = BIRD[0]
        self.dino_flying_rect = self.dino_flying.get_rect()
        self.dino_flying_rect.y = self.Y_POS

    def draw(self, screen: pygame.Surface):
        screen.blit(self.dino_flying, (self.dino_react.x, self.dino_react.y))
