from colorama import Fore
from GameMove import GameMove


class GameBoard(object):
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.score = [2, 2]
        self.playerColours = [Fore.BLUE, Fore.RED]
        self.playerCharacters = [".", self.playerColours[0] + "©" + Fore.RESET,
                                 self.playerColours[1] + "ø" + Fore.RESET]
        self.gameExtents = []
        self.moves = []
        for x in range(3, 5):
            self.fillLocation(1, x, x)
            self.fillLocation(2, 7 - x, x)

    def getDirections(self, x, y):
        directions = []
        for stepX in range(-1, 2):
            scanX = x + stepX
            if self.isPassedEdge(scanX):
                continue
            for stepY in range(-1, 2):
                if stepY == 0 and stepX == 0:
                    continue
                scanY = y + stepY
                if self.isPassedEdge(scanY):
                    continue
                direction = (stepX, stepY)
                directions.append(direction)

        return directions

    def fillLocation(self, playerNumber, x, y):
        self.board[x][y] = playerNumber

        location = (x, y)
        if location in self.gameExtents:
            self.gameExtents.remove(location)

        for direction in self.getDirections(x, y):
            scanX, scanY = x + direction[0], y + direction[1]
            if self.board[scanX][scanY] > 0:
                continue
            location = (scanX, scanY)
            if location in self.gameExtents:
                continue
            self.gameExtents.append(location)

    def getRowTerminator(self, x):
        if x == 7:
            return "\n"
        return " "

    def drawBoard(self, assessForPlayer):
        if assessForPlayer == 0:
            self.moves = []
        else:
            self.moves = self.assessBoard(assessForPlayer)

        for y in reversed(range(0, 8)):
            print(y, end=" ")
            for x in range(0, 8):
                print(self.getBoardCharacter(x, y),
                      end=self.getRowTerminator(x))
        print("  ", end="")

        for x in range(0, 8):
            print(x, end=self.getRowTerminator(x))

    def getBoardCharacter(self, x, y):
        piece = self.board[x][y]

        if piece > 0 or len(self.moves) == 0:
            return self.playerCharacters[piece]

        location = (x, y)
        if location not in self.moves:
            return "."

        move = self.moves[location]
        if move.flipCount == 0:
            return "."

        return self.getPlayerColour(move.playerNumber) + '.' + Fore.RESET

    def getPlayerCharacter(self, playerNumber):
        return self.playerCharacters[playerNumber]

    def getPlayerColour(self, playerNumber):
        return self.playerColours[playerNumber - 1]

    def getPlayerAtPosition(self, x, y):
        return self.board[x][y]

    def tryToMakeMove(self, playerNumber, x, y):
        location = (x, y)
        if location not in self.moves:
            return False

        move = self.moves[location]
        if move.flipCount == 0:
            return False

        for piece in move.overturned:
            pX, pY = piece[0], piece[1]
            self.board[pX][pY] = playerNumber

        self.fillLocation(playerNumber, x, y)
        self.score[playerNumber - 1] += move.flipCount + 1
        self.score[self.opponentNumber(playerNumber) - 1] -= move.flipCount

        return move.flipCount

    def assessBoard(self, playerNumber):
        moves = {}
        for location in self.gameExtents:
            moveX, moveY = location[0], location[1]

            move = self.assessMove(playerNumber, moveX, moveY)
            if len(move.overturned) == 0:
                continue
            moves[(moveX, moveY)] = move

        return moves

    def assessMove(self, playerNumber, x, y):
        allOverturned = []

        for direction in self.getDirections(x, y):
            stepX, stepY = direction[0], direction[1]
            overturned = self.assessRow(playerNumber, x, y, stepX, stepY)

            if len(overturned) > 0:
                allOverturned.extend(overturned)

        return GameMove(playerNumber, x, y, allOverturned)

    def opponentNumber(self, playerNumber):
        return 3 - playerNumber

    def assessRow(self, playerNumber, x, y, stepX, stepY):
        overturned = []
        while True:
            x += stepX
            if self.isPassedEdge(x):
                return []
            y += stepY
            if self.isPassedEdge(y):
                return []

            piece = self.board[x][y]
            if piece == 0:
                return []
            elif piece != playerNumber:
                overturned.append((x, y))
            else:
                break

        return overturned

    def isPassedEdge(self, coordinate):
        return coordinate < 0 or coordinate > 7

    def showScore(self):
        print("Score: {0} = {1}, {2} = {3}".format(self.getPlayerCharacter(1), self.score[0],
                                                   self.getPlayerCharacter(2), self.score[1]))
