import pygame
from random import randint

WIDTH, HEIGHT = 10, 10


class Ball(pygame.sprite.Sprite):
    def __init__(self, fore_color, x, y):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, fore_color, [0, 0, WIDTH, HEIGHT])
        self.delta_x = randint(4, 8)
        self.delta_y = randint(-8, 8)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

    def bounce_x(self):
        self.delta_x = -self.delta_x

    def bounce_y(self):
        self.delta_y = -self.delta_y

    def collision_check(self, sprite_list):
        for sprite in sprite_list:
            if pygame.sprite.collide_rect(self, sprite):
                self.bounce_x()
                self.delta_y = randint(-8, 8)
