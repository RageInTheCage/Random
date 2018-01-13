import os
import random
import pygame


class Apple(pygame.sprite.Sprite):
    def __init__(self, game_display, sprite_size):
        pygame.sprite.Sprite.__init__(self)
        image_path = os.path.join("graphics", "Apple.png")
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(image, (sprite_size, sprite_size))
        self.rect = self.image.get_rect()
        self.sprite_size = sprite_size
        self.move()
        self.timer = self.reset_timer()

    @staticmethod
    def reset_timer():
        return random.randint(150, 200)

    def move(self):
        self.location = [random.randint(0, 10), random.randint(0, 10)]
        self.rect.x = self.location[0] * self.sprite_size
        self.rect.y = self.location[1] * self.sprite_size

    def update(self, *args):
        self.timer -= 1

        if self.timer > 0:
            return

        self.move()
        self.timer = self.reset_timer()
