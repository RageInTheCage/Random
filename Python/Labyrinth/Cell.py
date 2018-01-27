from Direction import Direction
from Point import Point


class Cell(object):
    def __init__(self, maze, location, wall_colour):
        self.maze = maze
        self.location = Point(location)
        self.wall_colour = wall_colour
        self.wall_width = 3
        self.exits = [
            Direction.UP,
            Direction.LEFT,
            Direction.DOWN,
            Direction.RIGHT
        ]
        self.walls = {}

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
            self.location.offset(vector[0]),
            self.location.offset(vector[1])
        )
        self.exits.remove(wall_direction)

    def update(self):
        for wall in self.walls.values():
            self.maze.draw_line(wall, self.wall_colour, self.wall_width)
