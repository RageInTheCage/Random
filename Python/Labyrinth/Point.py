import math

from Direction import Direction


class Point:
    def __init__(self, location):
        self.location = location

    def move(self, direction):
        movements = self.movements()
        self.location = self.offset(movements[direction])

    def offset(self, offset):
        return self.location[0] + offset[0], self.location[1] + offset[1]

    def rotate_and_scale(self, origin, angle_in_radians, scale_factor):
        ox, oy = origin
        px = self.location[0] * scale_factor
        py = self.location[1] * scale_factor

        qx = ox + math.cos(angle_in_radians) * (px - ox) - math.sin(angle_in_radians) * (py - oy)
        qy = oy + math.sin(angle_in_radians) * (px - ox) + math.cos(angle_in_radians) * (py - oy)
        return qx, qy

    @staticmethod
    def movements():
        return {
            Direction.UP: (0, -1),
            Direction.LEFT: (-1, 0),
            Direction.DOWN: (0, 1),
            Direction.RIGHT: (1, 0)
        }
