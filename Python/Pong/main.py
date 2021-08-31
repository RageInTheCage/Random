import pygame
from Python.Pong.Ball import Ball
from Python.Pong.Paddle import Paddle
from Python.Pong.Score import Score


def create_sprites():
    paddle_a = Paddle(FORE_COLOR, 20, 200, pygame.K_q, pygame.K_a)
    paddle_b = Paddle(FORE_COLOR, 670, 200, pygame.K_UP, pygame.K_DOWN)
    ball = Ball(FORE_COLOR, 345, 195)
    sprite_list = pygame.sprite.Group()
    sprite_list.add(paddle_a, paddle_b, ball)
    return paddle_a, paddle_b, ball, sprite_list


def draw_net():
    pygame.draw.line(screen, FORE_COLOR, [349, 0], [349, 500], 5)


def initialise_screen():
    global BACK_COLOR, FORE_COLOR, FRAMES_PER_SECOND, screen
    BACK_COLOR = 200, 200, 255
    FORE_COLOR = 0, 0, 0
    screen_size = (700, 500)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Pong")


pygame.init()
initialise_screen()
FRAMES_PER_SECOND = 60

paddle_a, paddle_b, ball, sprite_list = create_sprites()

clock = pygame.time.Clock()

score_left = Score(screen, 250, FORE_COLOR)
score_right = Score(screen, 420, FORE_COLOR)
sprite_list.add(score_left, score_right)

game_is_underway = True
while game_is_underway:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_underway = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game_is_underway = False
    paddle_a.move(keys)
    paddle_b.move(keys)

    sprite_list.update()

    if ball.rect.x >= 690:
        score_left.increment()
        ball.bounce_x()
    elif ball.rect.x <= 0:
        score_right.increment()
        ball.bounce_x()

    if ball.rect.y > 490 or ball.rect.y < 0:
        ball.bounce_y()

    if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
        ball.bounce()

    screen.fill(BACK_COLOR)
    draw_net()
    sprite_list.draw(screen)
    pygame.display.flip()

    clock.tick(FRAMES_PER_SECOND)

pygame.quit()
