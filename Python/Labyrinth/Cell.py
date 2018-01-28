import pygame

from Direction import Direction
from Point import Point


class Cell(object):
    def __init__(self, maze, location, wall_colour):
        self.maze = maze
        self.point = Point(location)
        self.wall_colour = wall_colour
        self.end_colour = pygame.Color("blue")
        self.wall_width = 3
        self.exits = [
            Direction.UP,
            Direction.LEFT,
            Direction.DOWN,
            Direction.RIGHT
        ]
        self.walls = {}
        self._visible_ = False
        self.opacity = 0
        self._is_end_ = False

    @property
    def is_end(self):
        return self._is_end_

    @is_end.setter
    def is_end(self, value):
        self._is_end_ = value
        if value:
            self.visible = True

    @property
    def visible(self):
        return self._visible_

    @visible.setter
    def visible(self, value):
        self._visible_ = value
        if value:
            self.opacity = 1
        else:
            self.opacity = 0

    def add_wall(self, wall_direction: Direction):
        if wall_direction.value in self.walls:
            return

        vectors = (
            ((0, 0), (1, 0)),
            ((1, 0), (1, 1)),
            ((0, 1), (1, 1)),
            ((0, 0), (0, 1)),
        )
        vector = vectors[wall_direction.value]
        self.walls[wall_direction.value] = (
            self.point.offset(vector[0]),
            self.point.offset(vector[1])
        )
        self.exits.remove(wall_direction)

    def update(self):
        if not self.visible:
            return

        self.opacity -= .004
        if self.opacity <= 0:
            self.visible = False
            return

        if self.is_end:
            pointlist = ((0, 0), (1, 1), (1, 0))
            self.maze.draw_polygon(
                pointlist, self.point, 0, self.get_faded_colour(self.end_colour)
            )

        wall_colour = self.get_faded_colour(self.wall_colour)

        for wall in self.walls.values():
            self.maze.draw_line(wall, wall_colour, self.wall_width)

    def get_faded_colour(self, base_colour):
        wall_colour = []
        for element in base_colour:
            wall_colour.append(element * self.opacity)

        return wall_colour
