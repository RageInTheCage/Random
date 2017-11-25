import pygame
import random


class TextOverlay(object):
    def __init__(self, display, message, font_size=80, font_name='Impact'):
        self.display = display
        self.message = message
        font = pygame.font.SysFont(font_name, font_size)
        colour = (28, 28, 168)

        self.text_surface = font.render(message, False, colour)
        self.text_rectangle = self.text_surface.get_rect()

        display_size = self.display.get_rect()
        self.text_rectangle.left = (display_size.width - self.text_rectangle.width) / 2
        self.text_rectangle.top = display_size.height - self.text_rectangle.height * 2
        self.display_height = display_size.height

        self.animation_enabled = True
        self.acceleration = .2
        self.d_x = random.randint(-30, 31) / 10
        self.d_y = 0
        self.alpha = 255

    def show(self):
        self.display.blit(self.text_surface, self.text_rectangle)

    def animate(self):
        if not self.animation_enabled:
            return

        self.d_y += self.acceleration
        self.text_rectangle.left += self.d_x
        self.text_rectangle.top += self.d_y
        self.alpha -= 5
        self.text_surface.set_alpha(self.alpha)

    def is_gone(self):
        return self.text_rectangle.top > self.display_height or self.alpha <= 0
