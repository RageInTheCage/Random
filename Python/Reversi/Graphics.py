import pygame

from Animation import Animation
from AnimationFrameCollection import AnimationFrameCollection
from ScoreOverlay import ScoreOverlay
from TextOverlay import TextOverlay


def check_bounds(coordinate):
    if coordinate < 0:
        return 0
    if coordinate > 7:
        return 7
    return coordinate


class Graphics(object):
    def __init__(self, display_size, game_board):
        pygame.init()

        self.width = display_size[0]
        self.height = display_size[1]
        self.game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Reversi')
        self.game_board = game_board

        self.piece_size = int(self.height / 8)
        self.piece_frame_collection = AnimationFrameCollection(
            './Reversi Pieces/*.png', (self.piece_size, self.piece_size))
        self.animation_group = pygame.sprite.Group()
        self.pieces = {}
        self.cursor_location = [3, 3]
        self.cursor_visible = False

        self.background_colour = (222, 222, 224)
        self.move_colour = (255, 220, 211)
        self.clock = pygame.time.Clock()
        self.moves = []
        self.text_overlays = []
        self.score_overlay = ScoreOverlay(self.game_display)

    def add_piece(self, player_number, location):
        piece = self.add_animation(self.piece_frame_collection, index=7)
        self.set_piece_player_number(piece, player_number)
        piece.rect = self.get_location_rect(location)
        self.pieces[location] = piece
        return piece

    def add_animation(self, animation_frame_collection, index):
        animation = Animation(animation_frame_collection, index)
        self.animation_group.add(animation)
        return animation

    @staticmethod
    def set_piece_player_number(piece, player_number):
        piece.player_number = player_number
        piece.stop_at_index = (piece.max_index, 0)[player_number - 1]
        piece.step = (1, -1)[player_number - 1]

    def fill(self):
        self.game_display.fill(self.background_colour)

    def cursor_is_a_valid_move(self):
        key = (self.cursor_location[0], self.cursor_location[1])
        return key in self.moves

    def get_cursor_colour(self):
        if self.cursor_is_a_valid_move():
            return pygame.Color("green")
        return 255, 0, 0, 128

    def show_available_moves(self):
        if self.cursor_is_a_valid_move():
            return

        for key, move in self.moves.items():
            self.draw_rectangle(move.location, self.move_colour)

    def draw_rectangle(self, location, colour):
        surface = pygame.Surface((self.piece_size, self.piece_size),
                                 pygame.SRCALPHA)
        surface.fill(colour)
        self.game_display.blit(surface, self.get_location_rect(location))

    def draw_cursor(self):
        self.draw_rectangle(self.cursor_location, self.get_cursor_colour())

    def preview_move(self):
        self.set_board_pieces()

        key = (self.cursor_location[0], self.cursor_location[1])
        if key not in self.moves:
            return

        move = self.moves[key]
        player_index = move.player_number - 1
        step = (1, -1)[player_index]
        max_index = self.piece_frame_collection.max_index
        frames = int(max_index / 3)
        stop_at_index = (max_index - frames, frames)[player_index]

        for location in move.overturned:
            piece = self.pieces[location]
            piece.step = step
            piece.stop_at_index = stop_at_index

    def get_location_rect(self, location):
        return (location[0] * self.piece_size, location[1] * self.piece_size,
                self.piece_size, self.piece_size)

    def draw_piece(self, player_number, x, y):
        if player_number == 0:
            return
        self.game_display.blit(self.pieces[player_number - 1], (x * self.piece_size, y * self.piece_size))

    def draw_pieces(self):
        self.animation_group.update()
        self.animation_group.draw(self.game_display)

    def set_board_pieces(self):
        for x in range(0, 8):
            for y in range(0, 8):
                location = (x, y)
                piece = self.get_piece_at(location)
                player_number = self.game_board.get_player_at(x, y)

                if piece:
                    if player_number == 0:
                        piece.kill()
                        del (self.pieces[location])
                    else:
                        self.set_piece_player_number(piece, player_number)
                    continue
                elif player_number != 0:
                    self.add_piece(player_number, location)

    def get_piece_at(self, location):
        if location in self.pieces.keys():
            return self.pieces[location]
        return None

    def update(self):
        self.fill()
        self.draw_pieces()

        if self.cursor_visible:
            self.show_available_moves()
            self.draw_cursor()

        self.animate_text_overlays()
        self.score_overlay.show()
        pygame.display.update()
        self.clock.tick(30)

    def ask_player_for_move(self, player_number):
        self.moves = self.game_board.assess_board(player_number)
        self.cursor_visible = True
        cursor_events = self.cursor_events()
        chosen = False

        while not chosen:
            for event in pygame.event.get():
                if self.process_cursor_keys(cursor_events, event) or self.process_mouse_clicks(event):
                    chosen = True
                    break

                if event.type == pygame.QUIT:
                    self.close()

            self.update()

        self.cursor_visible = False
        return tuple(self.cursor_location)

    def animate_winning_pieces(self, player_number):
        self.wait_for_animation(self.piece_frame_collection.max_index)

        index = 0
        for piece in self.pieces.values():
            if piece.player_number != player_number:
                piece.index = int(index)
                index += 0.3
                if index > self.piece_frame_collection.max_index:
                    index = 0
                piece.stop_at_index = None
                piece.enabled = True

    def wait_for_animation(self, frame_count=20):
        for frame in range(0, frame_count):
            self.update()
            self.quit_if_user_wants()

    @staticmethod
    def quit_if_user_wants():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def process_mouse_clicks(self, event):
        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            self.cursor_location[0] = check_bounds(int(position[0] / self.piece_size))
            self.cursor_location[1] = check_bounds(int(position[1] / self.piece_size))
            self.preview_move()
            return False

        return event.type == pygame.MOUSEBUTTONDOWN

    def process_cursor_keys(self, cursor_events, event):
        if not event.type == pygame.KEYDOWN:
            return False

        if event.key in cursor_events:
            vector = cursor_events[event.key]
            self.cursor_location[0] = check_bounds(self.cursor_location[0] + vector[0])
            self.cursor_location[1] = check_bounds(self.cursor_location[1] + vector[1])
            self.preview_move()
            return False

        return event.key in (pygame.K_RETURN, pygame.K_SPACE)

    def animate_text_overlays(self):
        for text_overlay in self.text_overlays:
            text_overlay.animate()
            text_overlay.show()
            if text_overlay.is_gone():
                self.text_overlays.remove(text_overlay)

    def animate_move(self, move):
        self.add_piece(move.player_number, move.location)
        self.wait_for_animation(10)

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
        ask_overlay = TextOverlay(self.game_display, question)
        ask_overlay.animation_enabled = False
        self.append_text_overlays(ask_overlay)

        pygame.event.clear()
        answer = None
        while not answer:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key in answers:
                    answer = event.key
                if event.type == pygame.QUIT:
                    pygame.quit()

        ask_overlay.animation_enabled = True
        return answer

    def say(self, message):
        print(message)
        new_overlay = TextOverlay(self.game_display, message)
        self.append_text_overlays(new_overlay)

    def append_text_overlays(self, new_overlay):
        if len(self.text_overlays) > 0:
            top_most_y = min(overlay.text_rectangle.top for overlay in self.text_overlays)
            new_top = top_most_y - new_overlay.text_rectangle.height
            max_top = (self.height - new_overlay.text_rectangle.height) / 2
            if new_top < max_top:
                new_top = max_top
                self.wait_for_animation()
            new_overlay.text_rectangle.top = new_top
        self.text_overlays.append(new_overlay)
