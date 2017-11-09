class HumanPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.opponentNumber = 3 - playerNumber
        self.board = gameBoard

    def makeMove(self):
        x = 4
        y = 6
        self.board.tryToMakeMove(self.playerNumber, x - 1, y - 1)
