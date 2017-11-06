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
        if self.positionIsEmpty(x, y):
            self.board[x][y] = playerNumber
            return True
        return False