from enum import Enum

import math


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def rotate_clockwise(self):
        index = self.value + 1
        if index > 3:
            index = 0

        return Direction(index)

    def rotate_anticlockwise(self):
        index = self.value - 1
        if index < 0:
            index = 3

        return Direction(index)

    @property
    def angle_in_radians(self):
        return self.value * math.pi / 2

    @property
    def opposite(self):
        index = self.value + 2
        if index > 3:
            index -= 4

        return Direction(index)
