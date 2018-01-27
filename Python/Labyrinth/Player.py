import pygame

from Cell import Direction
from Point import Point


class Player:
    def __init__(self, maze, location):
        self.maze = maze
        self.point = Point(location)

        self.vectors = self.__get_vectors()
        self.colour = pygame.Color("yellow")
        self.direction = Direction.UP

    def update(self):
        for vector in self.vectors:
            line = (
                self.point.offset(vector[0]),
                self.point.offset(vector[1])
            )
            self.maze.draw_line(line, self.colour, 3)

    @staticmethod
    def __get_vectors():
        return (
            ((0, 0), (1, 1)),
            ((0, 1), (1, 0))
        )

    def handle(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            current_cell = self.maze.cells[self.point.location]
            if self.direction not in current_cell.exits:
                return

            self.point.move(self.direction)
            return

        if event.key == pygame.K_LEFT:
            self.direction = self.direction.rotate_anticlockwise()
        elif event.key == pygame.K_RIGHT:
            self.direction = self.direction.rotate_clockwise()

        print(self.direction.name)