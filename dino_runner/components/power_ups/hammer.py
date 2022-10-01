import pygame
from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH


class Hammer:
    Y_POS = 100
    X_POS = SCREEN_WIDTH

    def __init__(self):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.timer = 10

    def update(self, game_speed, power_up):

        self.rect.x -= game_speed

        # if self.rect.x < -self.rect.width:
        #     power_up.pop()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    def show_timer(self):
        pass
