import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True


def has_user_quit(event):
    return event.type == KEYDOWN and event.key == K_ESCAPE

red = 0
green = 0
blue = 0
background_colour =(0, 0, 0)

def check_bounds(colour):
    if colour < 0:
        return 0
    if colour > 255:
        return 255
    return colour

steps_between_fill = 1000
fill_step = steps_between_fill
while running:
    for event in pygame.event.get():
        #print(event)
        running = has_user_quit(event) == False
        if event.type == MOUSEBUTTONDOWN and event.button == 4:
            red = check_bounds(red + 10)
        if event.type == MOUSEBUTTONDOWN and event.button == 5:
            red = check_bounds(red - 10)
        elif event.type == MOUSEMOTION:
            green = check_bounds(event.pos[0])
            blue = check_bounds(event.pos[1])

    position = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (red, green, blue), position, 50)
    fill_step -= 1
    if fill_step == 0:
        background_colour = (255 - red, 255 - green, 255 - blue)
        screen.fill(background_colour)
        fill_step = steps_between_fill
    pygame.display.flip()