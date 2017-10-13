class HumanPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.opponentNumber = 3 - playerNumber
        self.gameBoard = gameBoard
        self.height = len(gameBoard)
        self.width = len(gameBoard[0])

    def makeMove(self):
        print ('Player {0}''s turn.'.format(self.getPlayerLetter()))
        self.askPlayerForMove()

    def getPlayerLetter(self):
        if self.playerNumber == 1:
            return 'X'
        return 'O'

    def askPlayerForMove(self):
        print ('Enter co-ordinates:')
        
        waitingForValidInput = True
        while waitingForValidInput:
            x = self.askPlayerForCoordinate('x = ', self.width)
            y = self.askPlayerForCoordinate('y = ', self.height)

            if self.coordinateIsEmpty(x, y):
                waitingForValidInput = False
            else:
                print ('That space is taken dummy')
                
        self.gameBoard[x - 1][y - 1] = self.playerNumber

    def coordinateIsEmpty(self, x, y):
        return self.gameBoard[x - 1][y - 1] == 0

    def askPlayerForCoordinate(self, prompt, maximumValue):
        waitingForValidInput = True
        while waitingForValidInput:
            coordinate = input(prompt)
            if self.isCoordinateValid(coordinate, maximumValue):
                return int(coordinate)
            print ('You twerp, that was invalid')        
    
    def isCoordinateValid(self, value, maximumValue):
        try:
            integerValue = int(value)
        except:
            return False

        return integerValue in range(1, maximumValue + 1)
