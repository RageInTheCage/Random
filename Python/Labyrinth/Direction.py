from enum import Enum


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
