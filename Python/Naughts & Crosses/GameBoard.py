class GameBoard(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]

    def drawBoard(self):
        for y in reversed(range(0, self.height)):
            for x in range(0, self.width):
                playerNumber = self.board[x][y]
                print (self.getPlayerLetter(playerNumber), end=' ')
            print('\n')

    def getPlayerLetter(self, playerNumber):
        if playerNumber == 1:
            return 'X'
        if playerNumber == 2:
            return 'O'
        return '.'

    def positionIsEmpty(self, x, y):
        return self.board[x][y] == 0

    def getPlayerAtPosition(self, x, y):
        return self.board[x][y]
    
    def tryToMakeMove(self, x, y, playerNumber):
        if self.positionIsEmpty(x, y):
            self.board[x][y] = playerNumber
            return True
        return False

    def playerHasWon(self, playerNumber):
        if self.checkForStraightWin(playerNumber):
            return True
        return self.checkForWinDiagonally(playerNumber)

    def checkForStraightWin(self, playerNumber):
        for x in range(0, self.width):
            countColumn, countRow = 0, 0
            for y in range(0, self.height):
                if self.board[x][y] == playerNumber:
                    countColumn += 1
                if self.board[y][x] == playerNumber:
                    countRow += 1
            if countColumn == self.height:
                return True
            if countRow == self.width:
                return True
        
        return False

    def checkForWinDiagonally(self, playerNumber):
        count1, count2 = 0, 0
        for index in range(0, self.width):
            if self.board[index][index] == playerNumber:
                count1 += 1
            y = self.width - index - 1
            if self.board[index][y] == playerNumber:
                count2 += 1
        return count1 == self.width or count2 == self.width
