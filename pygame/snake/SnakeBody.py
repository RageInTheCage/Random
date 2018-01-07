import pygame


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, location, sprite_size):
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        image = pygame.image.load("graphics\SnakeBody.png").convert_alpha()
        self.image = pygame.transform.scale(image, (sprite_size, sprite_size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0] * sprite_size
        self.rect.y = location[1] * sprite_size
