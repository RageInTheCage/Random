import pygame


class Logo(pygame.sprite.DirtySprite):
    def __init__(self, draw_buffer, center, direction):
        pygame.sprite.DirtySprite.__init__(self)

        self.image = pygame.image.load("Diligenica.PNG")
        self.rect = self.image.get_rect(center=center)
        self.window_size = draw_buffer.get_size()
        self.direction = direction

    def update(self):
        x = (self.rect.center[0] + self.direction[0]) % self.window_size[0]
        y = (self.rect.center[1] + self.direction[1]) % self.window_size[1]
        self.rect.center = (x, y)
        self.dirty = True
