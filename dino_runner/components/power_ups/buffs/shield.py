import random

import pygame
from dino_runner.utils.constants import SHIELD, SHIELD_STATES


class Shield:
    def __init__(self, axle_y, axle_x):
        self.image = SHIELD
        self.rect = self.image.get_rect()
        self.rect.y = axle_y
        self.rect.x = axle_x

    def update(self, game, manager):
        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            manager.power_ups.pop()

    def activate(self, game, manager):
        game.player.shield = True
        game.player.hammer = False
        game.player.fly = False
        game.player.state = SHIELD_STATES
        manager.is_active = True
        manager.timer_out = 8

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
