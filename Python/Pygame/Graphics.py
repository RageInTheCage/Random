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
        self.piece_frame_collection = AnimationFrameCollection('../Reversi/Animation/*.png')
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

    def get_player_frame_index(self, player_number):
        if player_number == 1:
            return 0
        return self.cursor_animation.max_index

    def fill(self):
        self.game_display.fill(self.background_colour)

    def draw_rectangle(self, location, colour):
        self.game_display.fill(colour, (location[0] * self.piece_size, location[1] * self.piece_size,
                                        self.piece_size, self.piece_size))

    def position_cursor(self, player_number):
        self.cursor_animation.rect = (self.cursor[0] * self.piece_size,
                                      self.cursor[1] * self.piece_size,
                                      self.piece_size, self.piece_size)

        self.cursor_animation.stop_at_index = self.get_player_frame_index(player_number)

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

                    new_piece = self.add_animation(self.piece_frame_collection, index=7)
                    player_index = player_number - 1
                    new_piece.stop_at_index = (0, new_piece.max_index)[player_index]
                    new_piece.step = (-1, 1)[player_index]
                    new_piece.rect = self.cursor_animation.rect
                    location = (self.cursor[0], self.cursor[1])
                    self.pieces[location] = new_piece

                    random_piece_index = random.randint(1, len(self.pieces))
                    random_player_number = random.randint(1, 2)
                    piece = self.pieces[random_piece_index]


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
