import random
import pygame
import math

from Cell import Cell
from Direction import Direction


class Maze:
    def __init__(self, display, dimensions):
        self.display = display
        rectangle = display.get_rect()
        self.display_width = rectangle[2]
        self.display_height = rectangle[3]
        self.origin = (int(self.display_width / 2), int(self.display_height / 2))
        self.cells = self.__create_cells(dimensions)
        self.angle_in_radians = 0
        self.ange_step = 0.05
        self.scale = 10
        self.scale_factor = None

    def update(self):
        self.__change_perspective()
        for cell in self.cells.values():
            cell.update()

    def draw_line(self, line, colour, width):
        rotated_from = self.__rotate(self.origin, line[0], self.angle_in_radians, self.scale_factor)
        rotated_to = self.__rotate(self.origin, line[1], self.angle_in_radians, self.scale_factor)
        pygame.draw.line(self.display, colour, rotated_from, rotated_to, width)

    def __change_perspective(self):
        self.angle_in_radians += self.ange_step
        if self.ange_step > -.001:
            self.ange_step -= 0.01
        self.scale += .005
        self.scale_factor = self.display_width / self.scale

    @staticmethod
    def __rotate(origin, point, angle_in_radians, scale_factor):
        ox, oy = origin
        px = point[0] * scale_factor
        py = point[1] * scale_factor

        qx = ox + math.cos(angle_in_radians) * (px - ox) - math.sin(angle_in_radians) * (py - oy)
        qy = oy + math.sin(angle_in_radians) * (px - ox) + math.cos(angle_in_radians) * (py - oy)
        return qx, qy

    def __create_cells(self, dimensions):
        cells = {}
        wall_colour = (255, 0, 0)
        cells_wide, cells_high = dimensions

        for x in range(0, cells_wide):
            for y in range(0, cells_high):
                location = (x, y)
                new_cell = Cell(self, location, wall_colour)

                if x == 0:
                    new_cell.add_wall(Direction.LEFT)
                elif x == cells_wide - 1:
                    new_cell.add_wall(Direction.RIGHT)

                if y == 0:
                    new_cell.add_wall(Direction.UP)
                elif y == cells_high - 1:
                    new_cell.add_wall(Direction.DOWN)
                cells[location] = new_cell

        for cell in cells.values():
            if random.randint(0, 1) == 1:
                cell.add_wall(Direction.UP)
            else:
                cell.add_wall(Direction.RIGHT)

        return cells
