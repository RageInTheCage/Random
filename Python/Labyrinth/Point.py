from Direction import Direction


class Point:
    def __init__(self, location):
        self.location = location

    def move(self, direction):
        movements = self.movements()
        self.location = self.offset(movements[direction])

    def offset(self, offset):
        return self.location[0] + offset[0], self.location[1] + offset[1]

    @staticmethod
    def movements():
        return {
            Direction.UP: (0, -1),
            Direction.LEFT: (-1, 0),
            Direction.DOWN: (0, 1),
            Direction.RIGHT: (1, 0)
        }
