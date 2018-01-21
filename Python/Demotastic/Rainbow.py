import math

import pygame
from pygame.constants import *

from ColourPulse import ColourPulse


class Rainbow:
    def __init__(self, display):
        self.colour_pulse = ColourPulse()
        self.display = display
        self.y = 0
        size = display.get_rect()
        self.display_width = size[2]
        self.display_height = size[3]
        self.width = 40

    def handle(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.colour_pulse = ColourPulse()
        elif event.type == MOUSEMOTION:
            self.colour_pulse.animate()
            pygame.draw.line(self.display, self.colour_pulse.colour, (0, self.y), (self.display_width, self.y),
                             self.width)

            self.y += self.width
            if self.y > self.display_height:
                self.y = 0

    def update(self, center):
        self.width = int(center[1] / 20) + 1
