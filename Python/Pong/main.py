# Pong Game - Refactored from https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
import pygame
from Python.Pong.Ball import Ball
from Python.Pong.Net import Net
from Python.Pong.Paddle import Paddle
from Python.Pong.Score import Score


def create_sprites():
    paddle_a = Paddle(FORE_COLOR, 20, 200, pygame.K_q, pygame.K_a)
    paddle_b = Paddle(FORE_COLOR, 670, 200, pygame.K_UP, pygame.K_DOWN)
    score_left = Score(FORE_COLOR, 250)
    score_right = Score(FORE_COLOR, 420)
    ball = Ball(FORE_COLOR, 345, 195, score_left, score_right)
    net = Net(FORE_COLOR)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(paddle_a, paddle_b, score_left, score_right, ball, net)

    return paddle_a, paddle_b, score_left, score_right, ball, sprite_list


def initialise_screen():
    global BACK_COLOR, FORE_COLOR, screen
    BACK_COLOR = 200, 200, 255
    FORE_COLOR = 0, 0, 0
    screen_size = (700, 500)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Pong")


def has_user_quit(events, keys):
    for event in events:
        if event.type == pygame.QUIT:
            return True
    return keys[pygame.K_ESCAPE]


def main():
    initialise_screen()
    frames_per_second = 60
    paddle_a, paddle_b, score_left, score_right, ball, sprite_list = create_sprites()
    clock = pygame.time.Clock()
    game_is_underway = True
    while game_is_underway:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        paddle_a.move_on_keypress(keys)
        paddle_b.move_on_keypress(keys)
        sprite_list.update()
        ball.collision_check([paddle_a, paddle_b])
        screen.fill(BACK_COLOR)
        sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(frames_per_second)
        game_is_underway = not has_user_quit(events, keys)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
