import random
import pygame
from Logo import Logo


def still_running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

    return True


def create_draw_buffer():
    pygame.init()
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    window_size = 800, 600
    return pygame.display.set_mode(window_size)


def center_screen():
    return [size / 2 for size in draw_buffer.get_size()]


def random_screen_location():
    size = draw_buffer.get_size()
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    return x, y


def random_direction():
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    return x, y


def create_background():
    surface = pygame.Surface(draw_buffer.get_size())
    surface.fill((250, 255, 255))
    return surface


def create_dirty_sprites(count=1):
    dirty_sprites = pygame.sprite.LayeredDirty()

    for x in range(0, count):
        logo = Logo(draw_buffer, random_screen_location(), random_direction())
        dirty_sprites.add(logo)

    dirty_sprites.clear(draw_buffer, background)

    return dirty_sprites


draw_buffer = create_draw_buffer()
background = create_background()
sprites = create_dirty_sprites(1)
clock = pygame.time.Clock()

while still_running():
    sprites.update()
    rectangles = sprites.draw(draw_buffer)
    clock.tick(24)
    pygame.display.update(rectangles)

pygame.quit()
