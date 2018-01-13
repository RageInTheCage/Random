import math

import pygame
from pygame.constants import *

from ColourPulse import ColourPulse


class PeacockFeather:
    def __init__(self, display):
        self.colour_pulse = ColourPulse()
        self.display = display
        self.offset = (0, 0)
        self.step = 1

    def handle(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.colour_pulse = ColourPulse()
        elif event.type == MOUSEMOTION:
            self.colour_pulse.animate()

    def update(self, center):
        radius = center[1]

        offset_center = (center[0] + self.offset[0], center[1] + self.offset[1])

        for degrees in range(0, 360, self.step):
            step_position = self.get_position(center, degrees, radius)
            pygame.draw.line(self.display, self.colour_pulse.colour, offset_center, step_position)

    def get_position(self, center, degrees, radius):
        return center[0] + math.sin(math.radians(degrees)) * radius + self.offset[0], \
               center[1] + math.cos(math.radians(degrees)) * radius + self.offset[1]
