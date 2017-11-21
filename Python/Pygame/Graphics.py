import pygame
from Sprites import Sprites
from TextOverlay import TextOverlay


def check_bounds(coordinate):
    if coordinate < 0:
        return 0
    if coordinate > 7:
        return 7
    return coordinate


class Graphics(object):
    def __init__(self, display_width, display_height):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Reversi')
        self.width = display_width
        self.height = display_height

        sprites = Sprites("Reversi Pieces.png", 2, 1)

        self.piece_size = int(display_height / 8)

        self.pieces = (
            sprites.get_tile(0, 0, self.piece_size, self.piece_size),
            sprites.get_tile(1, 0, self.piece_size, self.piece_size)
            )

        self.background_colour = (0, 0, 0)
        self.cursor_colour = (10, 10, 10)
        self.cursor = [3, 3]

        self.text_overlays = []


    def fill(self):
        self.game_display.fill(self.background_colour)

    def draw_piece(self, player_number, x, y):
        self.game_display.blit(self.pieces[player_number], (x * self.piece_size, y * self.piece_size))

    def draw_rectangle(self, location, colour):
        self.game_display.fill(colour, (location[0] * self.piece_size, location[1] * self.piece_size,
                                        self.piece_size, self.piece_size))

    def draw_cursor(self, player_number):
        self.draw_rectangle(self.cursor, self.cursor_colour)
        self.draw_piece(player_number, self.cursor[0], self.cursor[1])

    def game_loop(self):
        clock = pygame.time.Clock()
        player_number = 0

        for x in range(0, 8):
            for y in reversed(range(0, 8)):
                self.draw_piece(player_number, x, y)
        cursor_events = self.cursor_events()

        player_number = 1
        player_has_quit = False
        while not player_has_quit:
            for event in pygame.event.get():
                if self.process_cursor_keys(cursor_events, event) \
                         or self.process_mouse_clicks(event):
                    dialog = TextOverlay(self.game_display, "Everything ok (Y/N)?")
                    dialog.ask()
                    self.text_overlays.append(dialog)

                if event.type == pygame.QUIT:
                    player_has_quit = True

            self.fill()
            self.draw_cursor(player_number)
            self.animate_text_overlays()
            pygame.display.update()

            # Frames per second
            clock.tick(30)

        pygame.quit()
        quit()

    def process_mouse_clicks(self, event):
        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            self.cursor[0] = check_bounds(int(position[0] / self.piece_size))
            self.cursor[1] = check_bounds(int(position[1] / self.piece_size))
            return False

        return event.type == pygame.MOUSEBUTTONDOWN

    def process_cursor_keys(self, cursor_events, event):
        if event.type == pygame.KEYDOWN and event.key in cursor_events:
            vector = cursor_events[event.key]
            self.cursor[0] = check_bounds(self.cursor[0] + vector[0])
            self.cursor[1] = check_bounds(self.cursor[1] + vector[1])
            return False

    @staticmethod
    def cursor_events():
        return {
            pygame.K_RIGHT: (1, 0),
            pygame.K_LEFT: (-1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

    def add_text_overlay(self, message):
        self.text_overlays.append(TextOverlay(self.game_display, message, 3000))

    def animate_text_overlays(self):
        for text_overlay in self.text_overlays:
            text_overlay.animate()
            text_overlay.show()
            if text_overlay.is_gone():
                self.text_overlays.remove(text_overlay)
