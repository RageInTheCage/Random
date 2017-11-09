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
        for y in reversed(range(0, 8)):
            print(y + 1, end = ' ')
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

    def tryToMakeMove(self, x, y, playerNumber):
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

        totalFlipCount = 0
        for x in range(startFromX + stepX, stopX, stepX):
            flipCount = 0
            for y in range(startFromY + stepY, stopY, stepY):
                piece = self.board[x][y]
                if piece == opponent:
                    flipCount += 1
                elif piece == 0:
                    break
            if flipCount == 0:
                break

            for y in range(startFromY + stepY, stopY, stepY):
                piece = self.board[x][y]
                if piece == opponent:
                    self.board[x][y] = playerNumber
                else:
                    break

            totalFlipCount += flipCount

        return totalFlipCount




        if flipCount > 0:
            self.board[x][y] = playerNumber

        return flipCount

    def getStopCoordinate(self, step, startFrom):
        if step > 0:
            return 6
        elif step < 0:
            return 0
        return startFrom

