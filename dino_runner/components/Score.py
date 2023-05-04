import pygame


class Score:
    def __init__(self):
        self.score = 0
        self.max_score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2
        elif self.score > self.max_score:
            self.max_score = self.score

    def draw(self, screen ):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)
    
    def reset(self):
        self.score = 0