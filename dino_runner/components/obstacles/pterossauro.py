import random

import pygame
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Pterosaur():
    Y_POS = (250, 310)
    X_POS = SCREEN_WIDTH

    def __init__(self):
        pos = random.randint(0, 1)
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS[pos]
        self.rect.x = self.X_POS

        self.step_index = 0

    def update(self, game_speed, obstacle):
        self.run(game_speed, obstacle)

        if self.step_index >= 10:
            self.step_index = 0

    def run(self, game_speed, obstacle):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]

        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacle.pop()

        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
