import math

import pygame
from pygame.constants import *

from ColourPulse import ColourPulse


class Spiral:
    def __init__(self, display):
        self.outer = ColourPulse()
        self.inner = ColourPulse()
        self.display = display
        self.offset = (0, 0)
        self.step = 2
        self.start_degrees = 0
        self.width = 10

    def handle(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.outer = ColourPulse()
        elif event.type == MOUSEMOTION:
            self.outer.animate()

            self.start_degrees += 45
            if self.start_degrees > 360:
                self.start_degrees = 0

    def update(self, center):
        radius = 0
        radius_step = center[1] / 500
        previous = None

        self.inner.animate()

        for revolution in range(0, 3):
            for degrees in range(0, 360, self.step):
                inner_position = self.get_position(center, degrees, radius / 4 * 3)
                outer_position = self.get_position(center, degrees, radius)

                pygame.draw.line(self.display, self.inner.colour, inner_position, outer_position)
                if previous:
                    pygame.draw.line(self.display, self.outer.colour, previous, outer_position, self.width)

                previous = outer_position
                radius += radius_step

    def get_position(self, center, degrees, radius):
        return center[0] + math.sin(math.radians(degrees + self.start_degrees)) * radius + self.offset[0], \
               center[1] + math.cos(math.radians(degrees + self.start_degrees)) * radius + self.offset[1]
