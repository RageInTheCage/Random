import random


class AIPlayer(object):
    def __init__(self, player_number, game_board):
        self.playerNumber = player_number
        self.opponentNumber = 3 - player_number
        self.board = game_board
        self.moveNumber = 1

    def make_move(self):
        print(f'Player {self.playerNumber}: "I am thinking about move {self.moveNumber}..."')

        if self.moveNumber == 1:
            self.choose_a_free_corner()
        elif self.moveNumber == 2:
            if not self.fill_gap_if_possible(self.playerNumber):
                if not self.choose_opposite_corner_if_possible():
                    self.choose_a_free_corner()
        elif self.moveNumber == 3:
            if not self.fill_gap_if_possible(self.opponentNumber):
                if not self.fill_gap_if_possible(self.playerNumber):
                    self.choose_a_free_corner()
        elif self.moveNumber == 4:
            if not self.fill_gap_if_possible(self.playerNumber):
                if not self.fill_gap_if_possible(self.opponentNumber):
                    self.choose_a_free_corner()
        else:
            self.choose_free_space()

        self.moveNumber += 1

    def choose_a_free_corner(self):
        print('choose_a_free_corner')
        all_corners = [(0, 0),
                       (self.board.width - 1, 0),
                       (0, self.board.height - 1),
                       (self.board.width - 1, self.board.height - 1)]
        random.shuffle(all_corners)
        for corner in all_corners:
            if self.try_to_make_move(corner[0], corner[1]):
                if self.moveNumber == 1:
                    self.corner_from_first_move = corner
                return True
        return False

    def choose_opposite_corner_if_possible(self):
        print('choose_opposite_corner_if_possible')
        x = self.corner_from_first_move[0]
        y = self.corner_from_first_move[1]
        return self.try_to_make_move(2 - x, 2 - y)

    def fill_gap_if_possible(self, find_player_number):
        if self.try_to_fill_straight_gap(find_player_number):
            return True
        return self.try_to_fill_diagonal_gap(find_player_number)

    def try_to_fill_straight_gap(self, find_player_number):
        print('try_to_fill_straight_gap')

        column_gap_x, column_gap_y, row_gap_x, row_gap_y = None, None, None, None

        for x in range(0, self.board.width):
            count_column, count_row = 0, 0
            for y in range(0, self.board.height):
                xy_position = self.board.get_player_at_position(x, y)
                if xy_position == 0:
                    column_gap_x, column_gap_y = x, y
                elif xy_position == find_player_number:
                    count_column += 1

                yxposition = self.board.get_player_at_position(y, x)
                if yxposition == find_player_number:
                    count_row += 1
                elif yxposition == 0:
                    row_gap_x, row_gap_y = y, x

            if self.gap_was_filled(count_column, column_gap_x, column_gap_y):
                return True
            if self.gap_was_filled(count_row, row_gap_x, row_gap_y):
                return True

        return False

    def try_to_fill_diagonal_gap(self, find_player_number):
        print('try_to_fill_diagonal_gap')

        count1, count2 = 0, 0
        gap1_x, gap1_y, gap2_x, gap2_y = None, None, None, None

        for index in range(0, self.board.width):
            position1 = self.board.get_player_at_position(index, index)
            if position1 == 0:
                gap1_x, gap1_y = index, index
            elif position1 == find_player_number:
                count1 += 1

            y = self.board.width - index - 1
            position2 = self.board.get_player_at_position(index, y)
            if position2 == 0:
                gap2_x, gap2_y = index, y
            elif position2 == find_player_number:
                count2 += 1

        if self.gap_was_filled(count1, gap1_x, gap1_y):
            return True

        return self.gap_was_filled(count2, gap2_x, gap2_y)

    def gap_was_filled(self, count, x, y):
        if count == 2 and x is not None:
            return self.try_to_make_move(x, y)
        return False

    def choose_free_space(self):
        print('choose_free_space')

        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                if self.try_to_make_move(x, y):
                    return True
        return False

    def try_to_make_move(self, x, y):
        return self.board.try_to_make_move(x, y, self.playerNumber)
