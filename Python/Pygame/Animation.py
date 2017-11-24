import random
import pygame
import sys
import glob

def load_image(name):
    image = pygame.image.load(name).convert()
    return image


class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super(Animation, self).__init__()
        self.images = []

        for image_file_path in glob.glob('../Reversi/Animation/*.png'):
            self.images.append(load_image(image_file_path))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.images[0].get_rect()

    def update(self):
        """This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower."""
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    white = (222, 222, 224)
    screen.fill(white)

    my_sprite = Animation()
    my_group = pygame.sprite.Group(my_sprite)

    for index in range(1, 64):
        extra_sprite = Animation()
        location = (
            random.randint(0, 700),
            random.randint(0, 700)
        )
        extra_sprite.index = random.randint(0, 16)
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

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        screen.fill(white)
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
