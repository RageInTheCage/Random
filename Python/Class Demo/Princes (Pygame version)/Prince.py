import pygame


class Prince:
    def __init__(self, name, son_of=None):
        self.name = name
        self.son = son_of
        self.final_location = None
        self.screen = None
        self.speech_location = None
        self.text_location = None
        self.announcement = None
        self.font = None
        self.image = pygame.image.load("Prince.png")
        self.speech_bubble = None
        self.text_surface = None
        if son_of:
            self.current_location = son_of.current_location.copy()
        else:
            self.current_location = [0, 0]

    def announce(self):
        self.announcement = "I am {}".format(self.name)
        if self.son:
            self.announcement += ", son of {}".format(self.son.name)

        size = self.image.get_rect()
        self.speech_location = self.final_location[0] + size.width / 3 * 2, self.final_location[1] + size.height / 4
        self.text_location = self.speech_location[0] + 80, self.speech_location[1] + 20
        self.text_surface = self.font.render(self.announcement, True, (0, 80, 0))

        self.speech_bubble = pygame.image.load("Speech Bubble.png")
        text_width = self.text_surface.get_rect().width
        self.speech_bubble = pygame.transform.scale(self.speech_bubble, (text_width + 100, 66))

    def set_graphics(self, screen, font, location):
        self.screen = screen
        self.font = font
        self.final_location = location

    def move_to_location(self):
        if self.current_location[0] < self.final_location[0]:
            self.current_location[0] += 2
        if self.current_location[1] < self.final_location[1]:
            self.current_location[1] += 1

    def draw(self):
        self.move_to_location()
        self.screen.blit(self.image, self.current_location)

        if self.speech_bubble is None:
            return

        self.screen.blit(self.speech_bubble, self.speech_location)
        self.screen.blit(self.text_surface, self.text_location)
