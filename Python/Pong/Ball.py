import pygame
from random import randint

WIDTH, HEIGHT = 10, 10


class Ball(pygame.sprite.Sprite):
    def __init__(self, fore_color, x, y, score_left, score_right):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, fore_color, [0, 0, WIDTH, HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.move(x, y)

        self.delta_x = randint(4, 8)
        self.delta_y = randint(-8, 8)
        self.score_left = score_left
        self.score_right = score_right

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        if self.rect.y > 490 or self.rect.y < 0:
            self.bounce_y()

    def collision_check(self, sprite_list):
        for sprite in sprite_list:
            if pygame.sprite.collide_rect(self, sprite):
                self.bounce_x()
                self.delta_y = randint(-8, 8)

        if self.rect.x >= 690:
            self.score_left.increment()
            self.bounce_x()
        elif self.rect.x <= 0:
            self.score_right.increment()
            self.bounce_x()

    def bounce_x(self):
        self.delta_x = -self.delta_x

    def bounce_y(self):
        self.delta_y = -self.delta_y
