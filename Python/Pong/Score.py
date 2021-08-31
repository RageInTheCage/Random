import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, fore_color, x):
        super().__init__()

        self.fore_color = fore_color
        self.score = 0
        self.font = pygame.font.Font(None, 74)
        self.update()
        self.rect = self.image.get_rect().move(x, 10)

    def update(self):
        self.image = self.font.render(str(self.score), 1, self.fore_color)

    def increment(self):
        self.score += 1
