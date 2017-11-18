import pygame
from Sprites import Sprites

class Graphics(object):
    def __init__(self, display_width, display_height):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Reversi')

        sprites = Sprites("Reversi Pieces.png", 2, 1)

        self.piece_size = int(display_height / 8)

        self.pieces = (
            sprites.get_tile(0, 0, self.piece_size, self.piece_size),
            sprites.get_tile(1, 0, self.piece_size, self.piece_size)
            )

        self.cursor = [3, 3]


    def draw_piece(self, player_number, x, y):
        self.game_display.blit(self.pieces[player_number], (x * self.piece_size, y * self.piece_size))

    def game_loop(self):
        clock = pygame.time.Clock()

        player_number = 0
        for x in range(0, 8):
            for y in reversed(range(0, 8)):
                self.draw_piece(player_number, x, y)

        cursor_events = self.cursor_events()

        player_number = 1
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key in cursor_events:
                    self.draw_piece(1 - player_number, self.cursor[0], self.cursor[1])
                    vector = cursor_events[event.key]
                    self.cursor[0] = self.check_bounds(self.cursor[0] + vector[0])
                    self.cursor[1] = self.check_bounds(self.cursor[1] + vector[1])
                    self.draw_piece(player_number, self.cursor[0], self.cursor[1])

                if event.type == pygame.MOUSEMOTION:
                    self.draw_piece(1 - player_number, self.cursor[0], self.cursor[1])
                    position = pygame.mouse.get_pos()
                    self.cursor[0] = self.check_bounds(int(position[0] / self.piece_size))
                    self.cursor[1] = self.check_bounds(int(position[1] / self.piece_size))
                    self.draw_piece(player_number, self.cursor[0], self.cursor[1])

                if event.type == pygame.QUIT:
                    game_over = True

            pygame.display.update()

            # Frames per second
            clock.tick(10)

        pygame.quit()
        quit()

    def check_bounds(self, coordinate):
        if coordinate < 0:
            return 0
        if coordinate > 7:
            return 7
        return coordinate

    def cursor_events(self):
        return {
            pygame.K_RIGHT: (1, 0),
            pygame.K_LEFT: (-1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

