import pygame


class ScoreOverlay(object):
    def __init__(self, display):
        self.text_surface = None
        self.text_rectangle = None
        self.display = display
        self.font = pygame.font.SysFont("Impact", 40)
        self.colour = (28, 28, 168)

    def refresh(self, players):
        score_text = "{0}: {1}, {2}: {3}".format(
            players[0].name, players[0].score,
            players[1].name, players[1].score
        )
        self.set_text(score_text)

    def show_winner(self, message, players):
        score = [players[0].score, players[1].score]
        score.sort()
        score_text = "{0}:  {1} to {2}".format(
            message,
            score[1],
            score[0]
        )
        self.set_text(score_text)

    def set_text(self, score_text):
        self.text_surface = self.font.render(score_text, False, self.colour)
        self.text_surface.set_alpha(150)
        self.text_rectangle = self.text_surface.get_rect()
        display_size = self.display.get_rect()
        margin_left = self.text_rectangle.height / 3
        self.text_rectangle.left = margin_left
        self.text_rectangle.top = display_size.height - self.text_rectangle.height - margin_left

    def show(self):
        if self.text_surface is None:
            return
        self.display.blit(self.text_surface, self.text_rectangle)
