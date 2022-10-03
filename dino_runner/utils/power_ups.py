import random

from dino_runner.components.power_ups.buffs.hammer import Hammer
from dino_runner.components.power_ups.buffs.life import Life
from dino_runner.components.power_ups.buffs.replace_dino import ReplaceDino
from dino_runner.components.power_ups.buffs.shield import Shield
from dino_runner.components.power_ups.buffs.speed import Speed
from dino_runner.utils.constants import SCREEN_WIDTH

AXLE_Y = random.randint(80, 270)
AXLE_X = SCREEN_WIDTH + random.randint(10, 1000)


def choice_power(manager, game):
    rand = random.randint(1, 1500)
    if game.game_speed >= 25:
        if rand == 270:
            manager.power_ups.append(Hammer(AXLE_Y, AXLE_X))
            manager.power_name = "Hammer"
        elif rand == 1433:
            manager.power_ups.append(Shield(AXLE_Y, AXLE_X))
            manager.power_name = "Shield"
        elif rand == 1129 and game.life_count <= 2:
            manager.power_ups.append(Life(AXLE_Y, AXLE_X))
        elif rand == 333 and game.game_speed >= 30:
            manager.power_ups.append(Speed(AXLE_Y, AXLE_X))
        elif rand == 456 and game.game_speed >= 30:
            manager.power_ups.append(ReplaceDino(AXLE_Y, AXLE_X))
            manager.power_name = "Flying"
