from GameBoard import GameBoard

def main():
    clearScreen()
    print('Welcome to Reversi')

    while True:
        playGame()
        if playersAreBored():
            break

def playersAreBored():
    while True:
        areTheyBored = input('Are you bored yet [y/n]? ').lower()
        if areTheyBored == 'y':
            print ('Bye then...')
            return True
        if areTheyBored == 'n':
            clearScreen()
            print ('Excellent!  Another game...')
            return False
        print ('Huh? ')

def playGame():
    global gameBoard
    gameBoard = GameBoard()
    playerNumber = 1
    while True:
        print ('Player {0}''s turn.'.format(gameBoard.getPlayerCharacter(playerNumber)))
        gameBoard.drawBoard()

        playerNumber = 3 - playerNumber
        break

def clearScreen():
    print ('\n' * 3)


main()