import pygame
from dino_runner.components.Score import Score

from dino_runner.components.dinosau import Dinosaur
from dino_runner.components.inBoard import In_Board

from dino_runner.components.obstacles.obstacleManager import ObstacleManager

from dino_runner.utils.constants import BG, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.inBoard = In_Board()
        self.death_count = 0

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def play(self):
        self.playing = True
        self.obstacle_manager.reset()
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
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed,self.player,self.on_death )
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
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

    def on_death(self):
        pygame.time.delay(500)
        self.playing = False
        self.death_count += 1
        self.score.reset()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        if self.death_count == 0:
            self.inBoard.board_play(SCREEN_WIDTH // 2 ,SCREEN_HEIGHT // 2)
        else:
            self.inBoard.board_reset(SCREEN_WIDTH // 2 ,SCREEN_HEIGHT // 2)
            self.inBoard.board_score()
            self.board_death_count()
            


        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()

    
    def board_death_count(self):
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render(f"Your deaths:  {self.death_count}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (700, 500)    
        self.screen.blit(text, text_rect)



