import pygame
from Sprites import Sprites
from TextOverlay import TextOverlay


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

        self.background_colour = (222, 222, 224)
        self.cursor_colour = (250, 230, 230)
        self.move_colour = (255, 220, 211)
        self.cursor = [3, 3]
        self.clock = pygame.time.Clock()
        self.moves = []
        self.text_overlays = []

    def fill(self):
        self.game_display.fill(self.background_colour)

    def show_moves(self):
        key = (self.cursor[0], self.cursor[1])
        if key in self.moves:
            self.cursor_colour = pygame.color.Color("green")
            move = self.moves[key]

            for piece in move.overturned:
                self.draw_rectangle(piece, self.cursor_colour)
            return
        self.cursor_colour = pygame.color.Color("red")

        for key, move in self.moves.items():
            self.draw_rectangle((move.x, move.y), self.move_colour)

    def draw_rectangle(self, location, colour):
        self.game_display.fill(colour, (location[0] * self.piece_size, location[1] * self.piece_size,
                                        self.piece_size, self.piece_size))

    def draw_cursor(self):
        self.draw_rectangle(self.cursor, self.cursor_colour)

    def draw_piece(self, player_number, x, y):
        if player_number == 0:
            return
        self.game_display.blit(self.pieces[player_number - 1], (x * self.piece_size, y * self.piece_size))

    def draw_board(self):
        for x in range(0, 8):
            for y in range(0, 8):
                self.draw_piece(self.game_board.get_player_at(x, y), x, y)

    def update(self):
        pygame.display.update()
        # Frames per second
        self.clock.tick(20)

    def ask_player_for_move(self, assess_for_player):
        if assess_for_player == 0:
            self.moves = []
        else:
            self.moves = self.game_board.assess_board(assess_for_player)

        cursor_events = self.cursor_events()

        chosen = False
        while not chosen:
            for event in pygame.event.get():
                chosen = self.process_cursor_keys(cursor_events, event) \
                         or self.process_mouse_clicks(event)

                if event.type == pygame.QUIT:
                    self.close()

            self.fill()
            self.show_moves()
            self.draw_cursor()
            self.draw_board()
            self.animate_text_overlays()
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
        if not event.type == pygame.KEYDOWN:
            return False

        if event.key in cursor_events:
            vector = cursor_events[event.key]
            self.cursor[0] = check_bounds(self.cursor[0] + vector[0])
            self.cursor[1] = check_bounds(self.cursor[1] + vector[1])
            return False

        return event.key in (pygame.K_RETURN, pygame.K_SPACE)

    def animate_text_overlays(self):
        for text_overlay in self.text_overlays:
            text_overlay.animate()
            text_overlay.show()
            if text_overlay.is_gone():
                self.text_overlays.remove(text_overlay)

    @staticmethod
    def close():
        pygame.quit()

    @staticmethod
    def cursor_events():
        return {
            pygame.K_RIGHT: (1, 0),
            pygame.K_LEFT: (-1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

    def ask(self, question, answers=(pygame.K_y, pygame.K_n)):
        self.fill()
        self.draw_board()
        ask_overlay = TextOverlay(self.game_display, question)
        ask_overlay.animation_enabled = False
        self.append_text_overlays(ask_overlay)

        pygame.event.clear()
        answer = None
        while not answer:
            self.fill()
            self.draw_board()
            self.animate_text_overlays()
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key in answers:
                    answer = event.key
                if event.type == pygame.QUIT:
                    pygame.quit()

        ask_overlay.animation_enabled = True
        return answer

    def say(self, message):
        new_overlay = TextOverlay(self.game_display, message)
        self.append_text_overlays(new_overlay)

    def append_text_overlays(self, new_overlay):
        if len(self.text_overlays) > 0:
            top_most_y = min(overlay.text_rectangle.top for overlay in self.text_overlays)
            new_top = top_most_y - new_overlay.text_rectangle.height
            max_top = (self.height - new_overlay.text_rectangle.height) / 2
            if new_top < max_top:
                new_top = max_top
            new_overlay.text_rectangle.top = new_top
        self.text_overlays.append(new_overlay)

