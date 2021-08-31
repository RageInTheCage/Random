import pygame

WIDTH, HEIGHT = 10, 100


class Paddle(pygame.sprite.Sprite):
    def __init__(self, fore_color, x, y, up_key, down_key):
        super().__init__()

        self.up_key = up_key
        self.down_key = down_key
        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, fore_color, [0, 0, WIDTH, HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_on_keypress(self, keys):
        if keys[self.up_key]:
            self.move_up()
        elif keys[self.down_key]:
            self.move_down()

    def move_up(self, pixels=5):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels=5):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400
