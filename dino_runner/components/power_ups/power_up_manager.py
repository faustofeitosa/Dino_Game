import random

import pygame
from dino_runner.utils.constants import DEFAULT_STATES, FPS, SCREEN_WIDTH
from dino_runner.utils.power_ups import choice_power


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.timer_out = 8
        self.is_active = False
        self.power_name = ""

    def update(self, game):
        if len(self.power_ups) == 0:
            choice_power(self, game)
        for power in self.power_ups:
            power.update(game, self)
            if game.player.dino_react.colliderect(power):
                power.activate(game, self)
                self.power_ups.remove(power)
                break
        if self.is_active:
            self.handle_time_powers(game)

    def draw(self, screen: pygame.Surface):
        for power in self.power_ups:
            power.draw(screen)

    def draw_timer(self, font_style, screen: pygame.Surface, is_dark=False):
        font = pygame.font.Font(font_style, 15)
        if is_dark:
            text = font.render(
                f"{self.power_name} expire in {round(self.timer_out)}", True, (255, 27, 28))
        else:
            text = font.render(
                f"{self.power_name} expire in {round(self.timer_out)}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (140, 50)
        screen.blit(text, text_rect)

    def reset_powers(self):
        self.power_ups = []

    def handle_time_powers(self, game):
        self.timer_out -= 1 / FPS
        power_timer = self.timer_out
        if power_timer <= 0:
            game.player.shield = False
            game.player.hammer = False
            game.player.fly = False
            game.player.state = DEFAULT_STATES
            self.timer_out = 8
            self.is_active = False
