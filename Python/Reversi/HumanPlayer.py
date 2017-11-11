class HumanPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.board = gameBoard

    def makeMove(self):
        print('Enter co-ordinates:')

        while True:
            x = self.askPlayerForCoordinate('x = ')
            y = self.askPlayerForCoordinate('y = ')

            flipCount = self.board.tryToMakeMove(self.playerNumber, x, y)

            if flipCount > 0:
                break
            print("That space doesn't overturn any {0} pieces.".format(self.board.getPlayerCharacter(self.board.opponentNumber(self.playerNumber))))

    def askPlayerForCoordinate(self, prompt):
        waitingForValidInput = True
        while waitingForValidInput:
            coordinate = input(prompt)
            if self.isCoordinateValid(coordinate):
                return int(coordinate)
            print('You twerp, that was invalid')

    def isCoordinateValid(self, value):
        try:
            integerValue = int(value)
        except:
            return False

        return integerValue in range(0, 8)
