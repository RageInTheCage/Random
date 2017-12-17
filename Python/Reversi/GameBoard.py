from colorama import Fore

from GameMove import GameMove


class GameBoard(object):
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.players = None
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

    @staticmethod
    def get_row_terminator(x):
        if x == 7:
            return Fore.RESET + '\n'
        return ' '

    def draw_ascii_board(self, assess_for_player):
        if assess_for_player == 0:
            self.moves = []
        else:
            self.moves = self.assess_board(assess_for_player)

        for y in range(0, 8):
            print(y, end=" ")
            for x in range(0, 8):
                print(self.get_ascii_board_character(x, y),
                      end=self.get_row_terminator(x))
        print("  ", end="")

        for x in range(0, 8):
            print(x, end=self.get_row_terminator(x))

    def get_ascii_board_character(self, x, y):
        piece = self.board[x][y]

        if piece > 0 or len(self.moves) == 0:
            if piece == 0:
                return '.'
            player = self.players[piece - 1]
            return player.colour + player.character

        location = (x, y)
        if location not in self.moves:
            return Fore.RESET + '.'

        move = self.moves[location]
        if move.flipCount == 0:
            return Fore.RESET + '.'

        return self.players[move.player_number - 1].colour + '.'

    def get_player_at(self, x, y):
        return self.board[x][y]

    def try_to_make_move(self, x, y):
        location = (x, y)
        if location not in self.moves:
            return None

        move = self.moves[location]
        self.fill_location(move.player_number, x, y)

        for piece in move.overturned:
            p_x, p_y = piece[0], piece[1]
            self.board[p_x][p_y] = move.player_number

        player = self.players[move.player_number - 1]
        player.score += move.flipCount + 1
        player.opponent.score -= move.flipCount

        return move

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

    @staticmethod
    def is_passed_edge(coordinate):
        return coordinate < 0 or coordinate > 7

    @staticmethod
    def show_score(players):
        print(
            "Score: {0} = {1}, {2} = {3}".format(
                players[0].name, players[0].score,
                players[1].name, players[1].score
                )
        )
