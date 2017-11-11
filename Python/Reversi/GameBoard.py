from colorama import Fore


class GameBoard(object):
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.score = [2, 2]

        for x in range(3, 5):
            self.board[x][x] = 1
            self.board[7 - x][x] = 2

    def getRowTerminator(self, x):
        if x == 7:
            return "\n"
        return " "

    def drawBoard(self):
        for y in reversed(range(0, 8)):
            print(y, end=' ')
            for x in range(0, 8):
                playerNumber = self.board[x][y]
                print(self.getPlayerCharacter(playerNumber), end=self.getRowTerminator(x))
        print('  ', end='')
        for x in range(0, 8):
            print(x, end=self.getRowTerminator(x))

    def getPlayerCharacter(self, playerNumber):
        if playerNumber == 1:
            return Fore.BLUE + "©" + Fore.RESET
        elif playerNumber == 2:
            return Fore.RED + "ø" + Fore.RESET
        return "."

    def positionIsEmpty(self, x, y):
        return self.board[x][y] == 0

    def getPlayerAtPosition(self, x, y):
        return self.board[x][y]

    def tryToMakeMove(self, playerNumber, x, y):
        if not self.positionIsEmpty(x, y):
            return False

        flipCount = self.overturnPieces(playerNumber, x, y)
        if flipCount > 0:
            self.board[x][y] = playerNumber
            self.score[playerNumber - 1] += flipCount + 1
            self.score[self.opponentNumber(playerNumber) - 1] -= flipCount

        return flipCount

    def overturnPieces(self, playerNumber, x, y):
        totalFlipCount = 0

        for stepX in range(-1, 2):
            for stepY in range(-1, 2):
                if not (stepY == 0 and stepX == 0):
                    totalFlipCount += self.overTurnFrom(playerNumber, x, y, stepX, stepY)

        return totalFlipCount

    def opponentNumber(self, playerNumber):
        return 3 - playerNumber

    def overTurnFrom(self, playerNumber, startFromX, startFromY, stepX, stepY):
        opponent = self.opponentNumber(playerNumber)
        x = startFromX
        y = startFromY
        flipCount = 0
        while True:
            x += stepX
            y += stepY
            if self.isPassedEdge(x) or self.isPassedEdge(y):
                flipCount = 0
                break

            piece = self.board[x][y]
            if piece == opponent:
                flipCount += 1
                continue
            elif piece == 0:
                flipCount = 0
            break

        if flipCount > 0:
            x = startFromX
            y = startFromY
            while True:
                x += stepX
                y += stepY
                if self.isPassedEdge(x) or self.isPassedEdge(y):
                    break

                piece = self.board[x][y]
                if piece == opponent:
                    self.board[x][y] = playerNumber
                else:
                    break

        return flipCount

    def isPassedEdge(self, coordinate):
        return coordinate < 0 or coordinate > 7

    def playerHasWon(self, playerNumber):
        opponent = self.opponentNumber(playerNumber)
        if self.score[opponent - 1] == 0: #Opponent wiped out
            return True

        totalScore = sum(self.score)
        if totalScore == 64 and self.score[opponent - 1] < self.score[playerNumber - 1]: #Board filled
            return True

        return False
