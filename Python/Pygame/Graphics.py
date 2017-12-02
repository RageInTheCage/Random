import random

import pygame

from Animation import Animation
from AnimationFrameCollection import AnimationFrameCollection
from TextOverlay import TextOverlay


def check_bounds(coordinate):
    if coordinate < 0:
        return 0
    if coordinate > 7:
        return 7
    return coordinate


class Graphics(object):
    def __init__(self, display_size):
        pygame.init()

        self.width = display_size[0]
        self.height = display_size[1]
        self.game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Reversi')

        self.piece_size = int(self.height / 8)
        self.piece_frame_collection = AnimationFrameCollection('../Reversi/Animation/*.png',
                                                               (self.piece_size, self.piece_size))
        self.animation_group = pygame.sprite.Group()
        self.pieces = {}
        self.cursor_animation = self.add_animation(self.piece_frame_collection, index=0)

        self.background_colour = (222, 222, 224)
        self.cursor_colour = (250, 230, 230)
        self.move_colour = (255, 220, 211)
        self.cursor = [3, 3]
        self.clock = pygame.time.Clock()
        self.text_overlays = []

    def add_animation(self, animation_frame_collection, index):
        animation = Animation(animation_frame_collection, index)
        self.animation_group.add(animation)
        return animation

    def fill(self):
        self.game_display.fill(self.background_colour)

    def draw_rectangle(self, location, colour):
        self.game_display.fill(colour, (location[0] * self.piece_size, location[1] * self.piece_size,
                                        self.piece_size, self.piece_size))

    def position_cursor(self, player_number):
        self.cursor_animation.rect = (self.cursor[0] * self.piece_size,
                                      self.cursor[1] * self.piece_size,
                                      self.piece_size, self.piece_size)

        self.set_piece_player_number(self.cursor_animation, player_number)

    def game_loop(self):
        clock = pygame.time.Clock()
        cursor_events = self.cursor_events()
        player_number = 1
        player_has_quit = False
        while not player_has_quit:
            for event in pygame.event.get():
                if self.process_cursor_keys(cursor_events, event) \
                        or self.process_mouse_clicks(event):
                    player_number = 3 - player_number

                    self.add_piece(player_number)

                    rand_piece = random.choice(list(self.pieces.values()))
                    self.set_piece_player_number(rand_piece, 3 - rand_piece.player_number)

                if event.type == pygame.QUIT:
                    player_has_quit = True

            self.fill()
            self.position_cursor(player_number)
            self.animation_group.update()
            self.animation_group.draw(self.game_display)
            self.animate_text_overlays()
            pygame.display.update()

            # Frames per second
            clock.tick(10)

        pygame.quit()
        quit()

    def add_piece(self, player_number):
        piece = self.add_animation(self.piece_frame_collection, index=7)
        self.set_piece_player_number(piece, player_number)
        piece.rect = self.cursor_animation.rect
        location = (self.cursor[0], self.cursor[1])
        self.pieces[location] = piece

    @staticmethod
    def set_piece_player_number(piece, player_number):
        piece.player_number = player_number
        piece.stop_at_index = (0, piece.max_index)[player_number - 1]
        piece.step = (-1, 1)[player_number - 1]

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
