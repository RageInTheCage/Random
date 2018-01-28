import pygame

from Cell import Direction
from Point import Point


class Player:
    def __init__(self, maze, location):
        self.maze = maze
        self.point = Point(location)
        self.colour = pygame.Color("yellow")
        self.direction = Direction.UP
        self.look()

    def look(self):
        directions = (
            self.direction,
            self.direction.rotate_clockwise(),
            self.direction.rotate_anticlockwise()
        )

        for direction in directions:
            visible_cell = self.current_cell
            for distance in range(0, 5):
                visible_cell.visible = True
                if direction not in visible_cell.exits:
                    break

                adjacent_point = visible_cell.point.get_adjacent_point(direction)
                visible_cell = self.maze.cells[adjacent_point]

    def update(self):
        self.maze.draw_polygon(self.__get_points(), self.point, self.direction.angle_in_radians,
                               self.colour)

    @staticmethod
    def __get_points():
        return (
            (.3, .9),
            (.5, .1),
            (.7, .9)
        )

    def handle(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.__move_if_possible(self.direction)
            return

        if event.key == pygame.K_DOWN:
            self.__move_if_possible(self.direction.opposite)
            return

        if event.key == pygame.K_LEFT:
            self.direction = self.direction.rotate_anticlockwise()
        elif event.key == pygame.K_RIGHT:
            self.direction = self.direction.rotate_clockwise()

        self.look()

    def __move_if_possible(self, direction):
        if direction not in self.current_cell.exits:
            return

        self.point.move(direction)
        self.look()
        if self.current_cell.is_end:
            self.current_cell.is_end = False
            self.maze.randomly_place_end(self.point, 20)

    @property
    def current_cell(self):
        return self.maze.cells[self.point.location]
