from dino_runner.utils.constants import BIRD


BIRD_POS = 250
class Bird:
    def __init__(self):
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.rect.y = BIRD_POS
        self.step = 0

    def update(self):
        self.image = BIRD[0] if self.step < 5 else BIRD[1]
        self.step += 1
