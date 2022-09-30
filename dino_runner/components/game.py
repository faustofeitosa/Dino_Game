import pygame
from dino_runner.components.Dino import Dino
from dino_runner.components.obstacles.obstacle_manage import ObstacleManager
from dino_runner.utils.constants import (BG, FPS, ICON, JUMPING, SCREEN_HEIGHT,
                                         SCREEN_WIDTH, TITLE)

FONT_STYLE = "freesansbold.ttf"


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.death_count = 0
        self.score_rank = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
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
        if self.points % 100 == 0 and self.game_speed < 60:
            self.game_speed += 1
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        if self.points > 700 and self.points < 1400:
            self.screen.fill((32, 28, 36))
            self.draw_score(True)
        else:
            self.screen.fill((255, 255, 255))
            self.draw_score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
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

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_message(self, message, pos_y, is_death=False):
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        font = pygame.font.Font(FONT_STYLE, 30)
        if is_death:
            text = font.render(message, True, (255, 27, 28))
        else:
            text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + pos_y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        # Dino
        self.screen.blit(
            JUMPING, (half_screen_width - 43.5, half_screen_height - 120))

        # Start
        if self.death_count == 0:
            self.draw_message("Press any key to start", 0)
        # Restart
        else:
            self.draw_message("Press any key to restart", 0)

        # Death
        self.draw_message(f"Deaths: {self.death_count}", 50, True)

        # Score
        self.draw_message(f"Your Score: {self.points}", 100)

        # High Score
        self.draw_message(f"Your High Score: {self.score_rank}", 150)

        pygame.display.update()
        self.handle_key_events_on_menu()
