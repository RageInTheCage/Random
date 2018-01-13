import random

import pygame
import os


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, location, sprite_size):
        pygame.sprite.Sprite.__init__(self)
        self.location = list(location)
        image_path = os.path.join("graphics", "SnakeBody.png")
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(image, (sprite_size, sprite_size))
        self.rect = self.image.get_rect()
        self.sprite_size = sprite_size
        self.place_body()

    def place_body(self):
        self.rect.x = self.location[0] * self.sprite_size + random.randint(-2, 2)
        self.rect.y = self.location[1] * self.sprite_size + random.randint(-2, 2)

    def update(self, *args):
        self.place_body()
