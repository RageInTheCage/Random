class HumanPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.opponentNumber = 3 - playerNumber
        self.board = gameBoard

    def makeMove(self):
        self.board.tryToMakeMove(3, 5, self.playerNumber)
