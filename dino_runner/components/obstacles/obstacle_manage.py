import random

import pygame
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_type = "SMALL" if random.randint(0, 1) == 0 else "LARGE"
            self.obstacles.append(Cactus(cactus_type))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_react.colliderect(obstacle):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen: pygame.Surface):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
