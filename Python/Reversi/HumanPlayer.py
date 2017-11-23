class HumanPlayer(object):
    def __init__(self, player_number, gameBoard):
        self.player_number = player_number
        self.board = gameBoard

    def make_move(self, graphics):
        print('Enter co-ordinates:')

        while True:
            cursor = graphics.ask_player_for_move(self.player_number)

            flip_count = self.board.try_to_make_move(self.player_number, cursor[0], cursor[1])

            if flip_count > 0:
                break

            opponent = self.board.opponent_number(self.player_number)
            graphics.say("Must overturn {0}".format(self.board.get_player_name(opponent)))
            print("That space doesn't overturn any {0} pieces.".format(self.board.get_player_character(opponent)))