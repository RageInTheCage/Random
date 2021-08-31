import pygame.sprite

WIDTH, HEIGHT = 5, 500


class Net(pygame.sprite.Sprite):
    def __init__(self, fore_color):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, fore_color, [0, 0, WIDTH, HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = 349
