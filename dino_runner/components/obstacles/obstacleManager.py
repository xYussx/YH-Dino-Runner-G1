from dino_runner.components.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.components.obstacles.largeCactus import LargeCactus

from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

import pygame

import random


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 0:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            #elif random.randint(0, 2) == 2:
                #self.obstacles.append(Bird)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
               pygame.time.delay(500)
               game.playing = False
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
