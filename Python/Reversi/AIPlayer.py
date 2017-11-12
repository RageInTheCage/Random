class AIPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.board = gameBoard


    def makeMove(self):
        playerCharacter = self.board.getPlayerCharacter(self.playerNumber)
        print('Player {0} is thinking...'.format(playerCharacter))

        self.board.assessBoard(self.playerNumber)
        move = next(iter(self.board.moves.values()))

        self.board.tryToMakeMove(self.playerNumber, move.x, move.y)
