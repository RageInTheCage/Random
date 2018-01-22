import random

import math
import pygame
from pygame.constants import *

from ColourPulse import ColourPulse


class Maze:
    def __init__(self, display):
        self.back_colour = (0, 0, 0)
        self.wall_colour = ColourPulse(205, 255)
        self.display = display
        rectangle = display.get_rect()
        self.display_width = rectangle[2]
        self.display_height = rectangle[3]
        self.wall_length = 40
        self.maze_height = 0
        self.maze_width = 0
        self.walls = {}
        self.initialise_maze()
        self.angle_in_radians = 0
        self.step = math.pi / 64
        self.origin = (int(self.display_width / 2), int(self.display_height / 2))
        self.rotating = False
        self.final_angle = self.angle_in_radians

    def handle(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.wall_colour.reset()
            self.initialise_maze()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.final_angle += math.pi / 2
                self.step = abs(self.step)
                self.rotating = True
            elif event.key == K_LEFT:
                self.final_angle -= math.pi / 2
                self.step = -abs(self.step)
                self.rotating = True
        #elif event.type == MOUSEMOTION:

    def update(self, center):
        if self.rotating:
            self.angle_in_radians += self.step
            if self.step > 0:
                if self.angle_in_radians + self.step > self.final_angle:
                    self.rotating = False
                    self.angle_in_radians = self.final_angle
            elif self.angle_in_radians - self.step < self.final_angle:
                self.rotating = False
                self.angle_in_radians = self.final_angle

        self.wall_colour.animate()
        self.wall_length = int(center[0] / 5) + 10
        self.draw_maze(self.origin)

    def draw_maze(self, origin):
        self.display.fill(self.back_colour)

        for wall_from, wall_to in self.walls.items():
            rotated_from = self.rotate(origin, wall_from, self.angle_in_radians, self.wall_length)
            rotated_to = self.rotate(origin, wall_to, self.angle_in_radians, self.wall_length)
            pygame.draw.line(self.display, self.wall_colour.colour, rotated_from, rotated_to, 1)

    def initialise_maze(self):
        self.maze_height = int(self.display_height / self.wall_length)
        self.maze_width = self.maze_height
        self.walls = {}

        for x in range(0, self.maze_width):
            for y in range(0, self.maze_height):
                if random.randint(0, 1) == 0:
                    line_to = (x, y + 1)
                else:
                    line_to = (x + 1, y)
                self.walls[(x, y)] = line_to

    @staticmethod
    def rotate(origin, point, angle_in_radians, scale):
        ox, oy = origin
        px = point[0] * scale
        py = point[1] * scale

        qx = ox + math.cos(angle_in_radians) * (px - ox) - math.sin(angle_in_radians) * (py - oy)
        qy = oy + math.sin(angle_in_radians) * (px - ox) + math.cos(angle_in_radians) * (py - oy)
        return qx, qy
