import random


class AIPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.board = gameBoard


    def makeMove(self):
        playerCharacter = self.board.getPlayerCharacter(self.playerNumber)
        print("Player {0} is thinking...".format(playerCharacter))

        self.board.assessBoard(self.playerNumber)

        bestMove = random.choice(self.getBestMoves())

        self.board.tryToMakeMove(self.playerNumber, bestMove.x, bestMove.y)

    def getMoveScore(self, move):
        moveScore = self.getLocationScore(move.x, move.y)
        for location in move.overturned:
            locationX = location[0]
            locationY = location[1]
            moveScore += self.getLocationScore(locationX, locationY)
        return moveScore

    def getLocationScore(self, x, y):
        if self.isCorner(x, y):
            return 20
        if self.isEdge(x, y):
            return 10
        if self.isInnerCorner(x, y) and self.isCornerUnprotected(x, y):
            return -10
        return 1

    def isCorner(self, x, y):
        return self.isCoordinateAnEdge(x) and self.isCoordinateAnEdge(y)

    def isEdge(self, x, y):
        if self.isCorner(x, y):
            return False
        return self.isCoordinateAnEdge(x) or self.isCoordinateAnEdge(y)

    def isCoordinateAnEdge(self, coordinate):
        return coordinate == 0 or coordinate == 7

    def isInnerCorner(self, x, y):
        return (x == 1 or x == 6) and (y == 1 or y == 6)

    def isCornerUnprotected(self, innerCornerX, innerCornerY):
        cornerX = self.getEdgeNearest(innerCornerX)
        cornerY = self.getEdgeNearest(innerCornerY)
        return self.board.getPlayerAtPosition(cornerX, cornerY) != self.playerNumber

    def getEdgeNearest(self, coordinate):
        if coordinate < 4:
            return 0
        return 7

    def getBestMoves(self):
        bestMoveScore = None
        bestMoves = []

        for key, move in self.board.moves.items():
            moveScore = self.getMoveScore(move)
            if bestMoveScore is None or moveScore > bestMoveScore:
                bestMoveScore = moveScore
                bestMoves = [move]
            elif moveScore == bestMoveScore:
                bestMoves.append(move)

        return bestMoves


