import math

from Direction import Direction


class Point:
    def __init__(self, location):
        self.location = location

    def move(self, direction):
        self.location = self.get_adjacent_point(direction)

    def get_adjacent_point(self, direction):
        movements = self.movements()
        return self.offset(movements[direction])

    def offset(self, offset):
        return self.x + offset[0], self.y + offset[1]

    def rotate_and_scale(self, origin, angle_in_radians, scale_factor):
        ox, oy = origin
        px = self.x * scale_factor
        py = self.y * scale_factor

        qx = ox + math.cos(angle_in_radians) * (px - ox) - math.sin(angle_in_radians) * (py - oy)
        qy = oy + math.sin(angle_in_radians) * (px - ox) + math.cos(angle_in_radians) * (py - oy)
        return qx, qy

    @property
    def x(self):
        return self.location[0]

    @property
    def y(self):
        return self.location[1]

    def distance_from(self, point):
        return math.hypot(self.x - point.x, self.y - point.y)

    @staticmethod
    def movements():
        return {
            Direction.UP: (0, -1),
            Direction.LEFT: (-1, 0),
            Direction.DOWN: (0, 1),
            Direction.RIGHT: (1, 0)
        }
