import pygame


class Dialog(object):
    def __init__(self, display, message, milliseconds, font_name='Impact', font_size=100):
        self.display = display
        font = pygame.font.SysFont(font_name, font_size)
        colour = (0, 0, 255)

        self.text_surface = font.render(message, True, colour)
        self.text_rectangle = self.text_surface.get_rect()

        display_size = self.display.get_rect()

        self.text_rectangle.left = (display_size.width - self.text_rectangle.width) / 2
        self.text_rectangle.top = display_size.height - self.text_rectangle.height

        self.hide_after_ticks = pygame.time.get_ticks() + milliseconds
        self.final_top = display_size.height

        self.acceleration = .2
        self.speed = 0

    def display_message(self):
        self.display.blit(self.text_surface, self.text_rectangle)

    def animate(self):
        self.speed += self.acceleration
        self.text_rectangle.top += self.speed

    def times_up(self):
        return self.text_rectangle.top > self.final_top or pygame.time.get_ticks() > self.hide_after_ticks
