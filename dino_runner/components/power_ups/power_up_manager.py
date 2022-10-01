import random

import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.timer_out = 10

    def update(self, game):
        if len(self.power_ups) == 0:
            if game.points % 100 == 0:
                self.power_ups.append(Shield())
        for power in self.power_ups:
            power.update(game, self)
            if game.player.dino_react.colliderect(power):
                game.player.shield = True
                self.power_ups.remove(power)
                break
        if game.player.shield:
            self.handle_time_powers(game)

    def draw(self, screen: pygame.Surface):
        for power in self.power_ups:
            power.draw(screen)

    def draw_timer(self, font_style, screen: pygame.Surface, is_dark=False):
        width_center = SCREEN_WIDTH // 2
        font = pygame.font.Font(font_style, 15)
        if is_dark:
            text = font.render(
                f"Shield expire in {round(self.timer_out)}", True, (255, 27, 28))
        else:
            text = font.render(
                f"Shield expire in {round(self.timer_out)}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width_center, 50)
        screen.blit(text, text_rect)

    def reset_powers(self):
        self.power_ups = []

    def handle_time_powers(self, game):
        self.timer_out -= 1 / 30
        timer_shield = self.timer_out
        if timer_shield <= 0:
            game.player.shield = False
            self.timer_out = 10
