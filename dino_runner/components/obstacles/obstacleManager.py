
from dino_runner.components.obstacles.cactus import Cactus


from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

import pygame

import random


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())
        
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()

            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []




    
