import os

import pygame

pygame.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "rsz_dinowallpaper.png"))

DINO_WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

SOUNDS = {
    "Jump": pygame.mixer.Sound(os.path.join(MUSIC_DIR, "sounds/jump_sound.wav")),
    "Death": pygame.mixer.Sound(os.path.join(MUSIC_DIR, "sounds/death_sound.wav")),
    "Score": pygame.mixer.Sound(os.path.join(MUSIC_DIR, "sounds/score_sound.wav"))
}


GAME_OVER_ICON = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

HEARTH_STATUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/alive.png")),
    HEART
]

DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

# HAMMER_ACTIVE =

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

CLOUDS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Clouds.png'))


SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

CLOCK = pygame.image.load(os.path.join(IMG_DIR, 'Other/Clock.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

DEFAULT_STATES = {
    "Run": RUNNING,
    "Jump": JUMPING,
    "Down": DUCKING,
}

SHIELD_STATES = {
    "Run": RUNNING_SHIELD,
    "Jump": JUMPING_SHIELD,
    "Down": DUCKING_SHIELD,
}

HAMMER_STATES = {
    "Run": RUNNING_HAMMER,
    "Jump": JUMPING_HAMMER,
    "Down": DUCKING_HAMMER,
}

PTEROSAUR_MODE = pygame.transform.scale(BIRD[1], (97/1.3, 68/1.3))

PTEROSAUR_STATE = [
    pygame.transform.flip(BIRD[0], True, False),
    pygame.transform.flip(BIRD[1], True, False)
]
