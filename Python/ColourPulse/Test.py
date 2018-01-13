import random
import pygame
from pygame.locals import *
from ColourPulse import ColourPulse

pygame.init()

display_info = pygame.display.Info()
screen = pygame.display.set_mode(
    (
        display_info.current_w,
        display_info.current_h
    )
)

running = True
background = ColourPulse()
colour_of_blobs = ColourPulse()
clock = pygame.time.Clock()
wobble_factor = 50
background_animate = False
blob_width = 0


def show_frames_per_second():
    font = pygame.font.Font(None, 30)
    fps = font.render(
        "FPS: {0:.4f}".format(clock.get_fps()),
        True,
        pygame.Color('white'),
        pygame.Color('black')
    )
    screen.blit(fps, (10, 10))


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 5:
                wobble_factor -= 5
                if wobble_factor < 1:
                    wobble_factor = 1
            elif event.button == 4:
                wobble_factor += 5
            elif event.button == 1:
                background_animate = not background_animate
            else:
                blob_width = 1 - blob_width

            colour_of_blobs = ColourPulse()

    if background_animate:
        background.animate()
        screen.fill(background.colour)

    mouse_position = pygame.mouse.get_pos()

    for echo in range(20):
        colour_of_blobs.animate()

        cursor_position = (
            mouse_position[0] + random.randint(-wobble_factor, wobble_factor),
            mouse_position[1] + random.randint(-wobble_factor, wobble_factor)
        )
        cursor_radius = random.randint(1, wobble_factor)
        pygame.draw.circle(
            screen, colour_of_blobs.colour,
            cursor_position, cursor_radius,
            blob_width
        )

    show_frames_per_second()

    pygame.display.flip()
    clock.tick(20)
