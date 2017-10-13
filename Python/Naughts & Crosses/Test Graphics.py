from graphics import *

def drawBoard(boardRectangle):
    boardRectangle.setOutline('blue')
    boardRectangle.draw(win)
    
    top = boardRectangle.p1.y
    bottom = boardRectangle.p2.y
    left = boardRectangle.p1.x
    right = boardRectangle.p2.x
    
    height = boardRectangle.p2.y - top
    cellSize = int(height / 3)
    boardSize = cellSize * 3
    
    for i in range(cellSize, cellSize * 3, cellSize):
        verticalLine = Line(Point(i + left, bottom), Point(i + left, top))
        verticalLine.draw(win)
        horizontalLine = Line(Point(left, i + top), Point(right, i + top))
        horizontalLine.draw(win)

height, width = 300, 300
win = GraphWin("Test", height, width)

margin = 10
boardRectangle = Rectangle(Point(margin, margin), Point(width - margin -1, width - margin -1))
drawBoard(boardRectangle)
