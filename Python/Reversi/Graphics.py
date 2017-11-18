import pygame
from Sprites import Sprites


def check_bounds(coordinate):
    if coordinate < 0:
        return 0
    if coordinate > 7:
        return 7
    return coordinate


def text_objects(message, font, color):
    surface = font.render(message, True, color)
    return surface, surface.get_rect()


class Graphics(object):
    def __init__(self, display_size, game_board):
        pygame.init()

        self.width = display_size[0]
        self.height = display_size[1]
        self.game_display = pygame.display.set_mode((self.width, self.height))
        self.game_board = game_board

        pygame.display.set_caption('Reversi')

        sprites = Sprites("Reversi Pieces.png", 2, 1)

        self.piece_size = int(self.height / 8)

        self.pieces = (
            sprites.get_tile(0, 0, self.piece_size, self.piece_size),
            sprites.get_tile(1, 0, self.piece_size, self.piece_size)
            )

        self.background_colour = (30, 30, 30)
        self.cursor = [3, 3]
        self.clock = pygame.time.Clock()

    def draw_piece(self, player_number, x, y):
        if player_number == 0:
            return
        self.game_display.blit(self.pieces[player_number - 1], (x * self.piece_size, y * self.piece_size))

    def draw_board(self):
        self.game_display.fill(self.background_colour)
        for x in range(0, 8):
            for y in range(0, 8):
                self.draw_piece(self.game_board.get_player_at(x, y), x, y)

    def update(self):
        pygame.display.update()
        # Frames per second
        self.clock.tick(10)

    def ask_player_for_move(self, player_number):
        self.display_message("Move please...")
        cursor_events = self.cursor_events()

        chosen = False
        while not chosen:
            for event in pygame.event.get():
                chosen = self.process_cursor_keys(cursor_events, event)\
                         or self.process_mouse_clicks(event)

                if event.type == pygame.QUIT:
                    pygame.quit()

            self.draw_board()
            self.draw_piece(player_number, self.cursor[0], self.cursor[1])
            self.update()

        return self.cursor

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

        return event.type == pygame.K_KP_ENTER

    def display_message(self, message):
        font = pygame.font.Font('freesansbold.ttf', 24)
        surface, rectangle = text_objects(message, font, (255, 0, 0))
        rectangle.center = (self.width / 2, self.height / 2)
        self.game_display.blit(surface, rectangle)
        pygame.display.update()
        pygame.time.delay(3000)

    @staticmethod
    def cursor_events():
        return {
            pygame.K_RIGHT: (1, 0),
            pygame.K_LEFT: (-1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

