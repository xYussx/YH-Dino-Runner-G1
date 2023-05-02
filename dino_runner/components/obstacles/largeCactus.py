import random

from dino_runner.components.obstacles.obstacles import Obstacle


LARGE_CACTUS_POS_Y = 310
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0 ,2)
        super().__init__(image, self.type)
        self.rect.y = LARGE_CACTUS_POS_Y


    