import pygame
from pygame.locals import *

from Maze import Maze
from Player import Player


def main():
    clock, display = initialise()
    maze = Maze(display, (30, 10))
    player = Player(maze, (4, 4))
    background_colour = (5, 5, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if has_user_quit(event):
                running = False
            player.handle(event)

        display.fill(background_colour)
        maze.update()
        player.update()
        pygame.display.update()
        clock.tick(15)


def initialise():
    pygame.init()
    display = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Labyrinth")
    clock = pygame.time.Clock()
    return clock, display


def has_user_quit(event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            return True
    elif event.type == QUIT:
        return True


if __name__ == "__main__":
    main()
