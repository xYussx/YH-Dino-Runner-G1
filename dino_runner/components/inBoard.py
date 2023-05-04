import pygame
from dino_runner.components.Score import Score
from dino_runner.components.dinosau import Dinosaur
from dino_runner.utils.constants import DINO_DEAD, DINO_START, RESET, SCREEN_HEIGHT, SCREEN_WIDTH


class InBoard:
    
    def __init__(self):
        self.score = Score()
        self.dinosau = Dinosaur()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        


    def board_play(self, center_x, center_y):
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(text, text_rect)
        self.screen.blit(DINO_START, (center_x - 49, center_y - 131))

    def board_reset(self, center_x, center_y):
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Over ----> Press any key to restart", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(text, text_rect)
        self.screen.blit(RESET, (center_x - 69, center_y - 131))

    def board_score(self, score):
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render(f"Your score: {score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (400, 400)    
        self.screen.blit(text, text_rect)

    def board_max_score(self, max_score):
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render(f"Max score: {max_score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (580, 500)    
        self.screen.blit(text, text_rect)
    