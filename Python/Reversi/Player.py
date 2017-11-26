from colorama import Fore


class Player:
    def __init__(self, player_number, game_board):
        self.number = player_number
        self.game_board = game_board

        index = player_number - 1
        self.colour = (Fore.RED, Fore.BLUE)[index]
        self.name = ('red', 'blue')[index]
        self.character = ('©', 'ø')[index]
        self.score = 2
