from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from GameBoard import GameBoard

def main():
    clearScreen()
    print ('Welcome to our Naughts & crosses game.  Do you feel lucky punk?')
    
    while True:
        playGame()
        if playersAreBored():
            break

def playGame():
    global gameBoard
    gameBoard = GameBoard(3, 3)
    players = getPlayers()
    
    playerNumber = 1
    for moveNumber in range(1, gameBoard.width * gameBoard.height):
        print ('Player {0}''s turn.'.format(gameBoard.getPlayerLetter(playerNumber)))
        
        gameBoard.drawBoard()

        players[playerNumber - 1].makeMove()

        if gameBoard.playerHasWon(playerNumber):
            finishGame(playerNumber)
            return

        clearScreen()
        playerNumber = 3 - playerNumber
    
    print ("It's a draw - how dull.")

def getPlayers():
    print("Which game mode do you wish to use?")
    choices = [('A', 'Computer vs Computer', getAiVsAiOpponents()),
               ('B', 'Human vs Human', getHumanVsHumanOpponents()),
               ('C', 'Computer vs Human', getAiVsHumanOpponents())]
    for choice in choices:
        print('{0} {1}'.format(choice[0], choice[1]))
    while True:
        gameMode = input(': ').upper()
        for choice in choices:
            if choice[0] == gameMode:
                return choice[2]

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
    print("Well done player {0}, you won!".format(gameBoard.getPlayerLetter(winningPlayer)))
    gameBoard.drawBoard()

def clearScreen():
    print ('\n' * 3)

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
