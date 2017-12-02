import random
import pygame
import sys
from AnimationFrameCollection import AnimationFrameCollection


class Animation(pygame.sprite.Sprite):
    def __init__(self, animation_frame_collection, index):
        super(Animation, self).__init__()

        self.images = animation_frame_collection.images
        self.index = index
        self.step = 1
        self.max_index = len(self.images) - 1
        self.image = self.images[self.index]
        self.rect = self.images[0].get_rect()
        self.enabled = True
        self.advance_method = self.bounce
        self.stop_at_index = None

    def update(self):
        """This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower."""
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    white = (222, 222, 224)
    screen.fill(white)
    sprite_collection = AnimationFrameCollection('../Reversi/Animation/*.png')
    my_sprite = Animation(sprite_collection, index=0)
    my_group = pygame.sprite.Group(my_sprite)

    for index in range(1, 3):
        extra_sprite = Animation(sprite_collection, index=random.randint(0, 16))
        location = (
            random.randint(0, 700),
            random.randint(0, 700)
        )
        extra_sprite.rect.center = location
        my_group.add(extra_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            my_sprite.rect.center = position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            extra_sprite = Animation(sprite_collection, index=0)
            extra_sprite.rect.center = pygame.mouse.get_pos()
            my_group.add(extra_sprite)


        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        screen.fill(white)
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
