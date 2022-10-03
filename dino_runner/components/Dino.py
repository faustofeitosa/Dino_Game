
import pygame
from dino_runner.utils.constants import DEFAULT_STATES, PTEROSAUR_STATE, SOUNDS
from pygame.sprite import Sprite


class Dino(Sprite):
    X_POS = 80
    Y_POS = 310

    JUMP_VEL = 7.5

    def __init__(self):
        self.state = DEFAULT_STATES
        self.dino = self.state["Run"][0]

        self.dino_react = self.dino.get_rect()
        self.dino_react.x = self.X_POS
        self.dino_react.y = self.Y_POS
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_down = False

        self.shield = False
        self.hammer = False
        self.fly = False
        self.up = self.Y_POS

        self.jump_vel = self.JUMP_VEL

    def update(self, event_key):
        jump_event = event_key[pygame.K_UP] or event_key[pygame.K_SPACE]
        down_event = event_key[pygame.K_DOWN]

        if self.fly:
            if jump_event:
                self.flying_up()
            elif down_event:
                self.flying_down()
            else:
                self.flying()
        else:
            if self.dino_run:
                self.run()
            elif self.dino_jump:
                self.jump()
            elif self.dino_down:
                self.down()

        if not self.fly:
            if jump_event:
                self.dino_jump = True
                self.dino_run = False
            elif down_event:
                self.dino_down = True
                self.dino_run = False
            elif not self.dino_jump:
                self.dino_run = True
                self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.dino = self.state["Run"][0] if self.step_index < 5 else self.state["Run"][1]
        self.dino_react = self.dino.get_rect()
        self.dino_react.x = self.X_POS
        self.dino_react.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.dino = self.state["Jump"]
        SOUNDS["Jump"].play()
        if self.dino_jump:
            self.dino_react.y -= self.jump_vel * 4
            self.jump_vel -= 0.7

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_react.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def down(self):
        self.dino = self.state["Down"][0] if self.step_index < 5 else self.state["Down"][1]
        # self.dino_react = self.dino.get_rect()
        # self.dino_react.x = self.X_POS
        self.dino_react.y = self.Y_POS + 40
        self.step_index += 1

    def flying(self):
        self.dino = PTEROSAUR_STATE[0] if self.step_index < 5 else PTEROSAUR_STATE[1]
        self.dino_react = self.dino.get_rect()
        self.dino_react.x = self.X_POS
        self.dino_react.y = self.up
        self.step_index += 1

    def flying_up(self):
        self.dino = PTEROSAUR_STATE[0] if self.step_index < 5 else PTEROSAUR_STATE[1]
        self.up -= 5
        self.dino_react.y = self.up
        self.step_index += 1

    def flying_down(self):
        self.dino = PTEROSAUR_STATE[0] if self.step_index < 5 else PTEROSAUR_STATE[1]
        self.up += 5
        self.dino_react.y = self.up
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.dino, (self.dino_react.x, self.dino_react.y))
