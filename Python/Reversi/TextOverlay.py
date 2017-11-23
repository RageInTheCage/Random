import pygame
import random


class TextOverlay(object):
    def __init__(self, display, message, font_size=70, font_name='Impact'):
        self.display = display
        font = pygame.font.SysFont(font_name, font_size)
        colour = (0, 0, 255)

        self.text_surface = font.render(message, True, colour)
        self.text_rectangle = self.text_surface.get_rect()

        display_size = self.display.get_rect()
        self.text_rectangle.left = (display_size.width - self.text_rectangle.width) / 2
        self.text_rectangle.top = display_size.height - self.text_rectangle.height * 2
        self.display_height = display_size.height

        self.acceleration = .2
        self.d_x = random.randint(-30, 31) / 10
        self.d_y = 0

    def ask(self, answers=(pygame.K_y, pygame.K_n)):
        self.show()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key in answers:
                    return event.key
                if event.type == pygame.QUIT:
                    pygame.quit()

    def show(self):
        self.display.blit(self.text_surface, self.text_rectangle)

    def animate(self):
        self.d_y += self.acceleration
        self.text_rectangle.left += self.d_x
        self.text_rectangle.top += self.d_y

    def is_gone(self):
        return self.text_rectangle.top > self.display_height
