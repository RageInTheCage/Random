class HumanPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.opponentNumber = 3 - playerNumber
        self.board = gameBoard

    def makeMove(self):
        print ('Player {0}''s turn.'.format(self.getPlayerLetter()))
        self.askPlayerForMove()

    def getPlayerLetter(self):
        if self.playerNumber == 1:
            return 'X'
        return 'O'

    def askPlayerForMove(self):
        print ('Enter co-ordinates:')
        
        while True:
            x = self.askPlayerForCoordinate('x = ', self.board.width) - 1
            y = self.askPlayerForCoordinate('y = ', self.board.height) - 1 

            if self.board.tryToMakeMove(x, y, self.playerNumber):
                break
            print ('That space is taken dummy')
        
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
