import pygame
import random


class Logo(pygame.sprite.DirtySprite):
    def __init__(self, draw_buffer, center, direction):
        pygame.sprite.DirtySprite.__init__(self)

        image= pygame.image.load("Diligenica.PNG")
        self.original_image = self.random_rescale(image)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=center)
        self.window_size = draw_buffer.get_size()
        self.direction = direction
        self.degrees = random.randrange(0, 90)

    @staticmethod
    def random_rescale(image):
        x, y = image.get_rect().screen_size
        new_x = random.randrange(int(x / 2), int(x * 1.75))
        new_y = (new_x / x) * y
        new_size = new_x, int(new_y)
        return pygame.transform.smoothscale(image, new_size)

    def nudge_coordinate(self, index):
        return (self.rect.center[index] + self.direction[index]) % self.window_size[index]

    def update(self):
        self.degrees += 1
        self.image = pygame.transform.rotate(self.original_image, self.degrees)
        x = self.nudge_coordinate(0)
        y = self.nudge_coordinate(1)
        self.rect.center = (x, y)
        self.dirty = True

