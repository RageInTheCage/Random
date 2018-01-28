import random
import pygame

from Cell import Cell
from Direction import Direction
from Point import Point


class Maze:
    def __init__(self, display, dimensions):
        self.display = display
        rectangle = display.get_rect()
        self.display_width = rectangle[2]
        self.display_height = rectangle[3]
        self.origin = (int(self.display_width / 2), int(self.display_height / 2))
        self.cells = self.__create_cells(dimensions)
        self.angle_in_radians = 0
        self.angle_step = 0.05
        self.scale = 90
        self.scale_factor = self.display_width / self.scale

    def update(self):
        self.__change_perspective()
        for cell in self.cells.values():
            cell.update()

    def draw_line(self, line, colour, width):
        point_from = Point(line[0])
        point_to = Point(line[1])
        rotated_from = point_from.rotate_and_scale(self.origin, self.angle_in_radians, self.scale_factor)
        rotated_to = point_to.rotate_and_scale(self.origin, self.angle_in_radians, self.scale_factor)
        pygame.draw.line(self.display, colour, rotated_from, rotated_to, width)

    def __change_perspective(self):
        self.angle_in_radians += self.angle_step
        if self.angle_step > -.002:
            self.angle_step -= 0.0005
        #self.scale += .2
        self.scale_factor = self.display_width / self.scale

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

        for location, cell in cells.items():
            if random.randint(0, 1) == 1:
                cell.add_wall(Direction.UP)
                adjacent_offset = (0, -1)
                adjacent_direction = Direction.DOWN
            else:
                cell.add_wall(Direction.RIGHT)
                adjacent_offset = (1, 0)
                adjacent_direction = Direction.LEFT

            adjacent_location = cell.point.offset(adjacent_offset)
            if adjacent_location in cells:
                adjacent_cell = cells[adjacent_location]
                adjacent_cell.add_wall(adjacent_direction)

        return cells
