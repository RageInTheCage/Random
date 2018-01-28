from Direction import Direction
from Point import Point


class Cell(object):
    def __init__(self, maze, location, wall_colour):
        self.maze = maze
        self.point = Point(location)
        self.wall_colour = wall_colour
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

        self.opacity -= .001
        if self.opacity <= 0:
            self.visible = False
            return

        wall_colour = []
        for element in self.wall_colour:
            wall_colour.append(element * self.opacity)

        for wall in self.walls.values():
            self.maze.draw_line(wall, wall_colour, self.wall_width)
