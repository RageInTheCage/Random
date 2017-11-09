class GameBoard(object):
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        for x in range(3, 5):
            self.board[x][x] = 1
            self.board[7-x][x] = 2

    def getRowTerminator(self, x):
        if x == 7:
            return "\n"
        return " "

    def drawBoard(self):
        for y in (range(0, 8)):
            print(8 - y, end = ' ')
            for x in range(0, 8):
                playerNumber = self.board[x][y]
                print(self.getPlayerCharacter(playerNumber), end=self.getRowTerminator(x))
        print('  ', end = '')
        for x in range(0, 8):
            print(x + 1, end=self.getRowTerminator(x))

    def getPlayerCharacter(self, playerNumber):
        if playerNumber == 1:
            return "©"
        elif playerNumber == 2:
            return "ø"
        return "."

    def positionIsEmpty(self, x, y):
        return self.board[x][y] == 0

    def getPlayerAtPosition(self, x, y):
        return self.board[x][y]

    def tryToMakeMove(self, playerNumber, x, y):
        if not self.positionIsEmpty(x, y):
            return False

        self.overturnPieces(playerNumber, x, y)
        self.board[x][y] = playerNumber

        return True

    def overturnPieces(self, playerNumber, x, y):
        for stepX in range(-1, 2):
            for stepY in range(-1, 2):
                if not (stepY == 0 and stepX == 0):
                    self.overTurnFrom(playerNumber, x, y, stepX, stepY)

    def overTurnFrom(self, playerNumber, startFromX, startFromY, stepX, stepY):
        stopX = self.getStopCoordinate(stepX, startFromX)
        stopY = self.getStopCoordinate(stepY, startFromY)
        opponent = 3 - playerNumber
        x = startFromX
        y = startFromY
        flipCount = 0
        while x != stopX and y != stopY:
            x += stepX
            y += stepY

            piece = self.board[x][y]
            if piece == opponent:
                flipCount += 1
            elif piece == 0:
                break

        if flipCount > 0:
            x = startFromX
            y = startFromY
            while x != stopX and y != stopY:
                piece = self.board[x][y]
                if piece == opponent:
                    self.board[x][y] = playerNumber
                else:
                    break
            self.board[x][y] = playerNumber

        return flipCount

    def getStopCoordinate(self, step, startFrom):
        if step > 0:
            return 6
        elif step < 0:
            return 0
        return startFrom

