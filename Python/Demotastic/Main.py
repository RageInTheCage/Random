import pygame
from pygame.locals import *

from Maze import Maze
from PeacockFeather import PeacockFeather
from Rainbow import Rainbow
from Spiral import Spiral


def main():
    pygame.init()

    display_info = pygame.display.Info()
    display = pygame.display.set_mode((display_info.current_w, display_info.current_h))
    pygame.display.set_caption("Demotastic")

    running = True
    clock = pygame.time.Clock()

    #animations = [
    #    Maze(display)
    #]
    animations = get_animation_array(display)
    animations.append(Rainbow(display))

    while running:
        running = handle_events(animations, display)
        mouse_position = pygame.mouse.get_pos()

        for animation in animations:
            animation.update(mouse_position)

        pygame.display.update()

        clock.tick(10)


def get_animation_array(display):
    animations = []
    flip_flop = True

    for y in range(0, 800, 400):
        for x in range(0, 1200, 400):
            if flip_flop:
                assert isinstance(display, object)
                animation = Spiral(display)
            else:
                animation = PeacockFeather(display)

            animation.offset = (x, y)
            animations.append(animation)
            flip_flop = not flip_flop

    return animations


def handle_events(animations, display):
    for event in pygame.event.get():
        if has_user_quit(event):
            return False

        if event.type == MOUSEBUTTONDOWN:
            display.fill((0, 0, 0))

        for animation in animations:
            animation.handle(event)

    return True


def has_user_quit(event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            return True
    elif event.type == QUIT:
        return True

    return False


main()
