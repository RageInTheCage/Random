import random
import pygame
import math

from Cell import Cell, Direction


def create_cells(cells_wide, cells_high):
    cells = {}
    for x in range(0, cells_wide):
        for y in range(0, cells_high):
            location = (x, y)
            new_cell = Cell(location)
            if x == 0:
                new_cell.add_wall(Direction.LEFT)
            elif x == cells_wide - 1:
                new_cell.add_wall(Direction.RIGHT)
            if y == 0:
                new_cell.add_wall(Direction.UP)
            elif y == cells_high - 1:
                new_cell.add_wall(Direction.DOWN)

            if random.randint(0, 1) == 1:
                new_cell.add_wall(Direction.UP)
            else:
                new_cell.add_wall(Direction.RIGHT)
            cells[location] = new_cell

    return cells


class Maze:
    def __init__(self, display):
        self.display = display
        rectangle = display.get_rect()
        display_width = rectangle[2]
        display_height = rectangle[3]
        self.origin = (int(display_width / 2), int(display_height / 2))

        self.cells = create_cells(60, 60)
        self.wall_colour = (255, 255, 255)
        self.angle_in_radians = 0
        self.wall_length = display_height / 20

    def update(self):
        self.angle_in_radians += 0.05
        for location, cell in self.cells.items():
            for line in cell.get_lines():
                rotated_from = self.rotate(self.origin, line[0], self.angle_in_radians, self.wall_length)
                rotated_to = self.rotate(self.origin, line[1], self.angle_in_radians, self.wall_length)
                pygame.draw.line(self.display, self.wall_colour, rotated_from, rotated_to, 3)

    @staticmethod
    def rotate(origin, point, angle_in_radians, scale):
        ox, oy = origin
        px = point[0] * scale
        py = point[1] * scale

        qx = ox + math.cos(angle_in_radians) * (px - ox) - math.sin(angle_in_radians) * (py - oy)
        qy = oy + math.sin(angle_in_radians) * (px - ox) + math.cos(angle_in_radians) * (py - oy)
        return qx, qy
