from pygame.sprite import Sprite

import pygame

from dino_runner.utils.constants import JUMPING, RUNNING

JUMP_VELOCITY = 8.5
DINO_RUN = "running"
DINO_JUMPING = "jumping"

class Dinosaur(Sprite):
    POS_X = 80
    POS_y = 110
    
    def __init__(self):
        self.image = RUNNING [0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_y
        self.step = 0 
        self.action = DINO_RUN
        self.jump_velocity = JUMP_VELOCITY

    def update(self, user_input):
        if self.action == DINO_RUN:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
            
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]  :
                self.action = DINO_JUMPING
            else:
                self.action = DINO_RUN
            
        if self.step >= 10:
            self.step = 0

            
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = 310
            self.action = DINO_RUN
            self.jump_velocity = JUMP_VELOCITY

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.step += 1

    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x , self.rect.y))


        



