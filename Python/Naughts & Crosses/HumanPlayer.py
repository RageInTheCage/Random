class HumanPlayer(object):
    def __init__(self, player_number, game_board):
        self.playerNumber = player_number
        self.opponentNumber = 3 - player_number
        self.board = game_board

    def make_move(self):
        print(f'Player {self.get_player_letter()}''s turn.')
        self.ask_player_for_move()

    def get_player_letter(self):
        if self.playerNumber == 1:
            return 'X'
        return 'O'

    def ask_player_for_move(self):
        print('Enter co-ordinates:')

        while True:
            x = self.ask_player_for_coordinate('x = ', self.board.width) - 1
            y = self.ask_player_for_coordinate('y = ', self.board.height) - 1

            if self.board.try_to_make_move(x, y, self.playerNumber):
                break
            print('That space is taken dummy')

    def ask_player_for_coordinate(self, prompt, maximum_value):
        waiting_for_valid_input = True
        while waiting_for_valid_input:
            coordinate = input(prompt)
            if self.is_coordinate_valid(coordinate, maximum_value):
                return int(coordinate)
            print('You twerp, that was invalid')

    @staticmethod
    def is_coordinate_valid(value, maximum_value):
        try:
            integer_value = int(value)
        except:
            return False

        return integer_value in range(1, maximum_value + 1)
