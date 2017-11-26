from Player import Player


class HumanPlayer(Player):
    def __init__(self, player_number, game_board):
        Player.__init__(self, player_number, game_board)

    def make_move(self, graphics):
        print('Enter co-ordinates:')

        while True:
            cursor = graphics.ask_player_for_move(self.number)

            flip_count = self.game_board.try_to_make_move(self.number, cursor[0], cursor[1])

            if flip_count > 0:
                break

            message = "Must overturn {0}".format(self.opponent.name)
            graphics.say(message)
            print(message)
