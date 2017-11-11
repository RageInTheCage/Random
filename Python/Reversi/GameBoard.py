from colorama import Fore, Back, Style


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

    def drawBoard(self, showFlipCountForPlayerNumber):
        for y in reversed(range(0, 8)):
            print(y, end=' ')
            for x in range(0, 8):
                piece = self.board[x][y]

                print(self.getBoardCharacter(x, y, showFlipCountForPlayerNumber), end=self.getRowTerminator(x))
        print('  ', end='')
        for x in range(0, 8):
            print(x, end=self.getRowTerminator(x))

    def getBoardCharacter(self, x, y, showFlipCountForPlayerNumber):
        piece = self.board[x][y]
        if piece > 0:
            return self.getPlayerCharacter(piece)

        if showFlipCountForPlayerNumber == 0:
            return "."

        flipCount = self.assessMove(showFlipCountForPlayerNumber, x, y, overturnPieces=False)
        if flipCount == 0:
            return Style.DIM + Fore.WHITE + "." + Style.RESET_ALL

        return Style.BRIGHT + Back.YELLOW + "." + Style.RESET_ALL

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

        totalFlipCount = self.assessMove(playerNumber, x, y, overturnPieces=True)
        if totalFlipCount > 0:
            self.board[x][y] = playerNumber
            self.score[playerNumber - 1] += totalFlipCount + 1
            self.score[self.opponentNumber(playerNumber) - 1] -= totalFlipCount

        return totalFlipCount

    def assessMove(self, playerNumber, x, y, overturnPieces):
        totalFlipCount = 0

        for stepX in range(-1, 2):
            for stepY in range(-1, 2):
                if not (stepY == 0 and stepX == 0):
                    flipCount = self.getFlipCount(playerNumber, x, y, stepX, stepY)
                    totalFlipCount += flipCount
                    if overturnPieces and flipCount > 0:
                        self.overturnRow(playerNumber, x, y, stepX, stepY)

        return totalFlipCount

    def opponentNumber(self, playerNumber):
        return 3 - playerNumber

    def getFlipCount(self, playerNumber, startFromX, startFromY, stepX, stepY):
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

        return flipCount

    def overturnRow(self, playerNumber, x, y, stepX, stepY):
        opponent = self.opponentNumber(playerNumber)
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

    def showScore(self):
        print("Score: {0} = {1}, {2} = {3}".format(self.getPlayerCharacter(1), self.score[0],
                                                   self.getPlayerCharacter(2), self.score[1]))
