import random

class AIPlayer(object):
    def __init__(self, playerNumber, gameBoard):
        self.playerNumber = playerNumber
        self.opponentNumber = 3 - playerNumber
        self.gameBoard = gameBoard
        self.height = len(gameBoard)
        self.width = len(gameBoard[0])
        self.moveNumber = 1

    def makeMove(self):
        print ('Player {0}: "I am thinking about move {1}..."'.format(
            self.playerNumber, self.moveNumber))

        if self.moveNumber == 1:
            self.chooseAFreeCorner()
        elif self.moveNumber == 2:
            if not self.fillGapIfPossible(self.playerNumber):
                if not self.chooseOppositeCornerIfPossible():
                    self.chooseAFreeCorner()
        elif self.moveNumber == 3:
            if not self.fillGapIfPossible(self.playerNumber):
                self.chooseAFreeCorner()
        elif self.moveNumber == 4:
            if not self.fillGapIfPossible(self.playerNumber):
                if not self.fillGapIfPossible(self.opponentNumber):
                    self.chooseFreeCorner()
        else:
            self.chooseFreeSpace()
                
        self.moveNumber += 1

    def chooseAFreeCorner(self):
        print ('chooseAFreeCorner')
        allCorners = [(0,0), (2,0), (0, 2), (2, 2)]
        random.shuffle(allCorners)
        for corner in allCorners:
            if self.tryToMakeMove(corner[0], corner[1]):
                if self.moveNumber == 1:
                    self.cornerFromFirstMove = corner
                return True
        return False
    
    def chooseOppositeCornerIfPossible(self):
        print ('chooseOppositeCornerIfPossible')
        x = self.cornerFromFirstMove[0]
        y = self.cornerFromFirstMove[1]
        return self.tryToMakeMove(2 - x, 2 - y)

    def tryToMakeMove(self, x, y):
        if self.gameBoard[x][y] == 0:
            self.gameBoard[x][y] = self.playerNumber
            return True
        return False

    def fillGapIfPossible(self, findPlayerNumber):
        if self.tryToFillStraightGap(findPlayerNumber):
            return True
        return self.tryToFillDiagonalGap(findPlayerNumber)
    
    def tryToFillStraightGap(self, findPlayerNumber):
        print ('tryToFillStraightGap')
        
        columnGapX, columnGapY, rowGapX, rowGapY = None, None, None, None
        
        for x in range(0, self.width):
            countColumn, countRow = 0, 0
            for y in range(0, self.height):
                xyPosition = self.gameBoard[x][y]
                if xyPosition == 0:
                    columnGapX, columnGapY = x, y
                elif xyPosition == findPlayerNumber:
                    countColumn += 1

                yxposition = self.gameBoard[y][x]
                if yxposition == findPlayerNumber:
                    countRow += 1
                elif yxposition == 0:
                    rowGapX, rowGapY = y, x

            if self.gapWasFilled(countColumn, columnGapX, columnGapY):
                return True
            if self.gapWasFilled(countRow, rowGapX, rowGapY):
                return True
            
        return False

    def tryToFillDiagonalGap(self, findPlayerNumber):
        print ('tryToFillDiagonalGap')
        
        count1, count2 = 0, 0
        gap1X, gap1Y, gap2X, gap2Y = None, None, None, None
        
        for index in range(0, self.width):
            position1 = self.gameBoard[index][index]
            if position1 == 0:
                gap1X, gap1Y = index, index
            elif position1 == findPlayerNumber:
                count1 += 1
            
            y = self.width - index - 1
            position2 = self.gameBoard[index][y]
            if position2 == 0:
                gap2X, gap2Y = index, y
            elif position2 == findPlayerNumber:
                count2 += 1

        if self.gapWasFilled(count1, gap1X, gap1Y):
            return True
        
        return self.gapWasFilled(count2, gap2X, gap2Y)
    
    def gapWasFilled(self, count, x, y):
        if count == 2 and x is not None:
            return self.tryToMakeMove(x, y)
        return False

    def chooseFreeSpace(self):
        print ('chooseFreeSpace')

        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.tryToMakeMove(x, y):
                    return True
        return False
