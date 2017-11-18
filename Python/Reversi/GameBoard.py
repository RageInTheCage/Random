from colorama import Fore
from GameMove import GameMove


class GameBoard(object):
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.score = [2, 2]
        self.playerColours = [Fore.RED, Fore.BLUE]
        self.player_characters = [".", self.playerColours[0] + "©" + Fore.RESET,
                                  self.playerColours[1] + "ø" + Fore.RESET]
        self.game_extents = []
        self.moves = []
        for x in range(3, 5):
            self.fill_location(1, x, x)
            self.fill_location(2, 7 - x, x)

    def get_directions(self, x, y):
        directions = []
        for step_x in range(-1, 2):
            scan_x = x + step_x
            if self.is_passed_edge(scan_x):
                continue
            for step_y in range(-1, 2):
                if step_y == 0 and step_x == 0:
                    continue
                scan_y = y + step_y
                if self.is_passed_edge(scan_y):
                    continue
                direction = (step_x, step_y)
                directions.append(direction)

        return directions

    def fill_location(self, player_number, x, y):
        self.board[x][y] = player_number

        location = (x, y)
        if location in self.game_extents:
            self.game_extents.remove(location)

        for direction in self.get_directions(x, y):
            scan_x, scan_y = x + direction[0], y + direction[1]
            if self.board[scan_x][scan_y] > 0:
                continue
            location = (scan_x, scan_y)
            if location in self.game_extents:
                continue
            self.game_extents.append(location)

    def get_row_terminator(self, x):
        if x == 7:
            return "\n"
        return " "

    def draw_ascii_board(self, assess_for_player):
        if assess_for_player == 0:
            self.moves = []
        else:
            self.moves = self.assess_board(assess_for_player)

        for y in range(0, 8):
            print(y, end=" ")
            for x in range(0, 8):
                print(self.get_board_character(x, y),
                      end=self.get_row_terminator(x))
        print("  ", end="")

        for x in range(0, 8):
            print(x, end=self.get_row_terminator(x))

    def get_board_character(self, x, y):
        piece = self.board[x][y]

        if piece > 0 or len(self.moves) == 0:
            return self.player_characters[piece]

        location = (x, y)
        if location not in self.moves:
            return "."

        move = self.moves[location]
        if move.flipCount == 0:
            return "."

        return self.get_player_colour(move.player_number) + '.' + Fore.RESET

    def get_player_character(self, player_number):
        return self.player_characters[player_number]

    def get_player_colour(self, player_number):
        return self.playerColours[player_number - 1]

    def get_player_at(self, x, y):
        return self.board[x][y]

    def try_to_make_move(self, player_number, x, y):
        location = (x, y)
        if location not in self.moves:
            return False

        move = self.moves[location]
        if move.flipCount == 0:
            return False

        for piece in move.overturned:
            pX, pY = piece[0], piece[1]
            self.board[pX][pY] = player_number

        self.fill_location(player_number, x, y)
        self.score[player_number - 1] += move.flipCount + 1
        self.score[self.opponent_number(player_number) - 1] -= move.flipCount

        return move.flipCount

    def assess_board(self, player_number):
        moves = {}
        for location in self.game_extents:
            move_x, move_y = location[0], location[1]

            move = self.assess_move(player_number, move_x, move_y)
            if len(move.overturned) == 0:
                continue
            moves[(move_x, move_y)] = move

        return moves

    def assess_move(self, player_number, x, y):
        all_overturned = []

        for direction in self.get_directions(x, y):
            step_x, step_y = direction[0], direction[1]
            overturned = self.assess_row(player_number, x, y, step_x, step_y)

            if len(overturned) > 0:
                all_overturned.extend(overturned)

        return GameMove(player_number, x, y, all_overturned)

    def opponent_number(self, player_number):
        return 3 - player_number

    def assess_row(self, player_number, x, y, step_x, step_y):
        overturned = []
        while True:
            x += step_x
            if self.is_passed_edge(x):
                return []
            y += step_y
            if self.is_passed_edge(y):
                return []

            piece = self.board[x][y]
            if piece == 0:
                return []
            elif piece != player_number:
                overturned.append((x, y))
            else:
                break

        return overturned

    def is_passed_edge(self, coordinate):
        return coordinate < 0 or coordinate > 7

    def show_score(self):
        print("Score: {0} = {1}, {2} = {3}".format(self.get_player_character(1), self.score[0],
                                                   self.get_player_character(2), self.score[1]))
