import os
import pygame
from pygame.locals import *
from SnakeBody import SnakeBody


def main():
    game_display = create_display()
    sprite_size = 50
    snake_head_location = [9, 5]
    snake_sprite_group, snake_list = create_snake(sprite_size, snake_head_location)
    background_colour = (0, 100, 0)
    running = True
    clock = pygame.time.Clock()
    cursor_events = {
        K_RIGHT: (1, 0),
        K_LEFT: (-1, 0),
        K_UP: (0, -1),
        K_DOWN: (0, 1)
    }
    snake_direction = [0, -1]
    max_snake_length = 15
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key in cursor_events:
                    snake_direction = cursor_events[event.key]
        snake_head_location[0] += snake_direction[0]
        snake_head_location[1] += snake_direction[1]
        add_to_snake(sprite_size, snake_head_location, snake_sprite_group, snake_list)
        remove_from_snake(snake_list, max_snake_length)
        game_display.fill(background_colour)
        snake_sprite_group.update()
        snake_sprite_group.draw(game_display)
        pygame.display.flip()
        clock.tick(10)


def create_display():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    game_display = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Snake')
    return game_display


def create_snake(sprite_size, snake_head_location):
    snake_sprite_group = pygame.sprite.Group()
    snake_body = SnakeBody(snake_head_location, sprite_size)
    snake_sprite_group.add(snake_body)
    snake_list = [snake_body]
    return snake_sprite_group, snake_list


def add_to_snake(sprite_size, snake_head_location, snake_sprite_group, snake_list):
    snake_body = SnakeBody(snake_head_location, sprite_size)
    snake_sprite_group.add(snake_body)
    snake_list.append(snake_body)


def remove_from_snake(snake_list, max_snake_length):
    if len(snake_list) <= max_snake_length:
        return
    snake_body = snake_list[0]
    snake_body.kill()
    snake_list.pop(0)


main()
