import random
import pygame


def get_random_location(screen):
    screen_size = screen.get_rect()
    x = random.randint(0, screen_size.width)
    y = random.randint(0, screen_size.height)
    return x, y


def get_random_color():
    red = get_random_channel()
    green = get_random_channel()
    blue = get_random_channel()
    return red, green, blue


def get_random_channel():
    return random.randint(0, 255)


def get_random_location_delta(screen, location):
    screen_size = screen.get_rect()
    x = get_single_delta(location[0], screen_size.width)
    y = get_single_delta(location[1], screen_size.height)
    return x, y


def get_single_delta(value, max_value, max_delta=20):
    value += random.randint(-max_delta, max_delta)
    if value < 0:
        return 0
    elif value > max_value:
        return max_value
    return value


def get_random_color_delta(color):
    color_delta = []
    for channel in color:
        color_delta.append(get_single_delta(channel, 255, 1))
    return color_delta


def get_random_width_delta(line_width):
    return get_single_delta(line_width, 100, 1)


def main():
    screen = pygame.display.set_mode()
    game_is_playing = True

    location = get_random_location(screen)
    color = get_random_color()
    line_width = random.randint(0, 10)

    while game_is_playing:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        game_is_playing = not keys[pygame.K_ESCAPE]

        next_location = get_random_location_delta(screen, location)
        pygame.draw.line(screen, color, location, next_location, line_width)
        color = get_random_color_delta(color)
        line_width = get_random_width_delta(line_width)
        location = next_location
        pygame.display.flip()


pygame.init()
main()
pygame.quit()
