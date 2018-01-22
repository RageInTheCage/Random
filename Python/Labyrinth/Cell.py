from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Cell(object):
    def __init__(self, location):
        self.location = location
        self.exits = [
            Direction.UP,
            Direction.DOWN,
            Direction.LEFT,
            Direction.RIGHT
        ]
        self.walls = {}

    def add_wall(self, wall_direction: Direction):
        if wall_direction.value in self.walls:
            return

        vectors = (
            ((0, 0), (1, 0)),
            ((0, 1), (1, 1)),
            ((0, 0), (0, 1)),
            ((1, 0), (1, 1))
        )
        vector = vectors[wall_direction.value]
        self.walls[wall_direction.value] = (
            self.add_location(vector[0]),
            self.add_location(vector[1])
        )
        self.exits.remove(wall_direction)

    def add_location(self, point):
        return point[0] + self.location[0], point[1] + self.location[1]

    def get_lines(self):
        return self.walls.values()
