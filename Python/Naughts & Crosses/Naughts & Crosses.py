from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer

def main():
    clearScreen()
    print ('Welcome to our Naughts & crosses game.  Do you feel lucky punk?')
    
    while True:
        playGame()
        if playersAreBored():
            break

def getPlayers():
    print("Which game mode do you wish to use?")
    choices = [('A', 'Computer vs Computer'),
               ('B', 'Player vs Player'),
               ('C', 'Computer vs Player')]
    for choice in choices:
        print('{0} {1}'.format(choice[0], choice[1]))
    gameMode = None
    while gameMode not in ('A', 'B', 'C'):
        gameMode = input(':  ').upper()
    if gameMode == 'A':
        return getAiVsAiOpponents()
    elif gameMode == 'B':
        return getHumanVsHumanOpponents()
    return getAiVsHumanOpponents()

def playGame():
    resetBoard()
    players = getPlayers()
    
    playerNumber = 1
    for moveNumber in range(1, 10):
        print ('Player {0}''s turn.'.format(getPlayerLetter(playerNumber)))
        
        drawBoard()

        players[playerNumber - 1].makeMove()

        if playerHasWon(playerNumber):
            finishGame(playerNumber)
            return

        clearScreen()
        playerNumber = 3 - playerNumber
    
    print ("It's a draw - how dull.")

def getAiVsHumanOpponents():
    return (
        AIPlayer(1, gameBoard),
        HumanPlayer(2, gameBoard)
        )

def getHumanVsHumanOpponents():
    return (
        HumanPlayer(1, gameBoard),
        HumanPlayer(2, gameBoard)        
        )

def getAiVsAiOpponents():
    p1 = AIPlayer(1, gameBoard)
    p2 = AIPlayer(2, gameBoard)
    return (p1, p2)

def finishGame(winningPlayer):
    clearScreen()
    print("Well done player {0}, you won!".format(getPlayerLetter(winningPlayer)))
    drawBoard()

def clearScreen():
    print ('\n' * 3)

def resetBoard():
    global width, height, gameBoard
    width, height = 3, 3;
    gameBoard = [[0 for x in range(width)] for y in range(height)]

def drawBoard():
    for y in reversed(range(0, height)):
        for x in range(0, width):
            playerNumber = gameBoard[x][y]
            print (getPlayerLetter(playerNumber), end=' ')
        print('\n')

def getPlayerLetter(playerNumber):
    if playerNumber == 1:
        return 'X'
    if playerNumber == 2:
        return 'O'
    return '.'

def playerHasWon(playerNumber):
    if checkForStraightWin(playerNumber):
        return True
    return checkForWinDiagonally(playerNumber)

def checkForStraightWin(playerNumber):
    for x in range(0, width):
        countColumn, countRow = 0, 0
        for y in range(0, height):
            if gameBoard[x][y] == playerNumber:
                countColumn += 1
            if gameBoard[y][x] == playerNumber:
                countRow += 1
        if countColumn == height:
            return True
        if countRow == width:
            return True
    
    return False

def checkForWinDiagonally(playerNumber):
    count1, count2 = 0, 0
    for index in range(0, width):
        if gameBoard[index][index] == playerNumber:
            count1 += 1
        y = width - index - 1
        if gameBoard[index][y] == playerNumber:
            count2 += 1
    return count1 == width or count2 == width

def playersAreBored():
    while True:
        areTheyBored = input('Are you bored yet [y/n]? ').lower()
        if areTheyBored == 'y':
            print ('Charming!  Bye then...')
            return True
        if areTheyBored == 'n':
            clearScreen()
            print ('Excellent!  Another game, goody...')
            return False
        print ('Huh? ')

main()
