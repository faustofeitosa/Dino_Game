import pygame
from dino_runner.components.Cloud import CloudManager
from dino_runner.components.Dino import Dino
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import (BG, DINO_WALLPAPER, FPS,
                                         GAME_OVER_ICON, HEARTH_STATUS, ICON,
                                         JUMPING, RESET, SCREEN_HEIGHT,
                                         SCREEN_WIDTH, SOUNDS, TITLE)

FONT_STYLE = "SuperMario256.ttf"


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = Dino()

        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.cloud = CloudManager()

        self.playing = False
        self.running = False
        self.game_speed = 20

        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.life_count = 3
        self.score_rank = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                if self.life_count == 0:
                    self.game_over()
                else:
                    self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_powers()
        self.cloud.reset_cloud()
        self.game_speed = 20
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.points += 1
        if self.points % 100 == 0 and self.game_speed <= 60:
            SOUNDS["Score"].play()
            self.game_speed += 1
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        draw_powers = self.player.shield or self.player.hammer or self.player.fly
        dark = self.points > 700 and self.points < 1400 or self.points > 3000 and self.points < 300
        if dark:
            self.screen.fill((32, 28, 36))
            self.draw_score(True)
            if draw_powers:
                self.power_up_manager.draw_timer(FONT_STYLE, self.screen, True)
        else:
            self.screen.fill((255, 255, 255))
            self.draw_score()
            if draw_powers:
                self.power_up_manager.draw_timer(FONT_STYLE, self.screen)
        self.draw_background()
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_hearth()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self, is_dark=False):
        font = pygame.font.Font(FONT_STYLE, 15)
        if is_dark:
            text = font.render(f"Points {self.points}", True, (250, 250, 250))
        else:
            text = font.render(f"Points {self.points}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_message(self, message, pos_y=0, is_dark=False):
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        font = pygame.font.Font(FONT_STYLE, 30)
        if is_dark:
            text = font.render(message, True, (255, 27, 28))
        else:
            text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + pos_y)
        self.screen.blit(text, text_rect)

    def draw_hearth(self):
        height = SCREEN_HEIGHT//2
        width = SCREEN_WIDTH//2

        status = HEARTH_STATUS
        if self.life_count == 1:
            self.screen.blit(status[1], (width + 5, height - 260))
            self.screen.blit(status[1], (width - 25, height - 260))
            self.screen.blit(status[0], (width - 55, height - 260))
        elif self.life_count == 2:
            self.screen.blit(status[1], (width + 5, height - 260))
            self.screen.blit(status[0], (width - 25, height - 260))
            self.screen.blit(status[0], (width - 55, height - 260))
        else:
            self.screen.blit(status[0], (width + 5, height - 260))
            self.screen.blit(status[0], (width - 25, height - 260))
            self.screen.blit(status[0], (width - 55, height - 260))

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        self.screen.blit(DINO_WALLPAPER, (half_screen_width -
                         43.5, half_screen_height - 140))

        if self.life_count == 3:
            self.draw_hearth()
            self.draw_message("Press any key to start")
        else:
            self.draw_hearth()
            self.draw_message("Press any key to restart")
            self.draw_message(f"Your Score: {self.points}", 50)
            self.draw_message(f"Your High Score: {self.score_rank}", 100)

            self.screen.blit(RESET, (half_screen_width -
                                     43.5, half_screen_height + 150))

        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self, game_over=False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    self.run()
            else:
                self.playing = False
                self.running = False

    def game_over(self):
        half_screen_height = SCREEN_HEIGHT//2
        image_width = GAME_OVER_ICON.get_width()
        self.screen.fill((255, 255, 255))

        self.screen.blit(
            GAME_OVER_ICON, (image_width, half_screen_height))
        pygame.display.update()
        self.handle_key_events_on_menu(True)
