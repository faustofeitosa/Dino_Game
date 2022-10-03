import random

import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.pterossauro import Pterosaur
from dino_runner.utils.constants import (DEFAULT_STATES, DINO_DEAD, DUCKING,
                                         SOUNDS)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0, 2)
            self.chose_obstacle(obstacle_type)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_react.colliderect(obstacle):
                if game.player.shield:
                    print("Protected")
                elif game.player.hammer:
                    self.obstacles.remove(obstacle)
                else:
                    SOUNDS["Death"].play()
                    self.end_game(game)
                break

    def draw(self, screen: pygame.Surface):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

    def end_game(self, game):
        game.player.dino = DINO_DEAD
        game.score_rank = game.points if game.points > game.score_rank else game.score_rank
        pygame.time.delay(1000)
        game.playing = False
        game.life_count -= 1
        game.player.hammer = False
        game.player.shield = False
        game.player.state = DEFAULT_STATES

    def chose_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            self.obstacles.append(Pterosaur())
        else:
            cactus_type = "SMALL" if random.randint(0, 1) == 0 else "LARGE"
            self.obstacles.append(Cactus(cactus_type))
