import random

import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.pterossauro import Pterosaur


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
                if not game.player.shield:
                    self.end_game(game)
                else:
                    self.obstacles.remove(obstacle)
                break

    def draw(self, screen: pygame.Surface):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

    def end_game(self, game):
        game.score_rank = game.points if game.points > game.score_rank else game.score_rank
        # game.player.dino = DEAD
        # print("You dead!")
        pygame.time.delay(1000)
        game.playing = False
        game.death_count += 1

    def chose_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            self.obstacles.append(Pterosaur())
        else:
            cactus_type = "SMALL" if random.randint(0, 1) == 0 else "LARGE"
            self.obstacles.append(Cactus(cactus_type))
