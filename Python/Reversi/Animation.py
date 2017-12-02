import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, animation_frame_collection, index):
        super(Animation, self).__init__()

        self.images = animation_frame_collection.images
        self.index = index
        self.step = 1
        self.max_index = animation_frame_collection.max_index
        self.image = self.images[self.index]
        self.rect = self.images[0].get_rect()
        self.enabled = True
        self.advance_method = self.bounce
        self.stop_at_index = None

    def update(self):
        self.enabled = self.index != self.stop_at_index

        if not self.enabled:
            return

        self.advance_method()
        self.image = self.images[self.index]

    def bounce(self):
        if self.index >= self.max_index:
            self.step = -1
        elif self.index <= 0:
            self.step = 1
        self.index += self.step

    def loop(self):
        next_index = self.index + self.step
        if next_index > self.max_index:
            self.index = 0
        elif next_index < 0:
            self.index = self.max_index
        else:
            self.index = next_index
