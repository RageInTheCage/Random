from Player import Player


class HumanPlayer(Player):
    def __init__(self, player_number, game_board):
        Player.__init__(self, player_number, game_board)

    def make_move(self, graphics):
        while True:
            cursor = graphics.ask_player_for_move(self.number)
            move = self.game_board.try_to_make_move(cursor[0], cursor[1])

            if move:
                return move

            message = "Must overturn {0}".format(self.opponent.name)
            graphics.say(message)
