class GameBoard(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]

    def draw_ascii_board(self):
        for y in reversed(range(0, self.height)):
            for x in range(0, self.width):
                player_number = self.board[x][y]
                print(self.get_player_letter(player_number), end=' ')
            print('\n')

    @staticmethod
    def get_player_letter(player_number):
        if player_number == 1:
            return 'X'
        if player_number == 2:
            return 'O'
        return '.'

    def position_is_empty(self, x, y):
        return self.board[x][y] == 0

    def get_player_at_position(self, x, y):
        return self.board[x][y]

    def try_to_make_move(self, x, y, player_number):
        if self.position_is_empty(x, y):
            self.board[x][y] = player_number
            return True
        return False

    def player_has_won(self, player_number):
        if self.check_for_straight_win(player_number):
            return True
        return self.check_for_win_diagonally(player_number)

    def check_for_straight_win(self, player_number):
        for x in range(0, self.width):
            count_column, count_row = 0, 0
            for y in range(0, self.height):
                if self.board[x][y] == player_number:
                    count_column += 1
                if self.board[y][x] == player_number:
                    count_row += 1
            if count_column == self.height:
                return True
            if count_row == self.width:
                return True

        return False

    def check_for_win_diagonally(self, player_number):
        count1, count2 = 0, 0
        for index in range(0, self.width):
            if self.board[index][index] == player_number:
                count1 += 1
            y = self.width - index - 1
            if self.board[index][y] == player_number:
                count2 += 1
        return count1 == self.width or count2 == self.width
