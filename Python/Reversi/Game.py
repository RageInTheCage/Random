from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer


def main():
    clearScreen()
    print("Welcome to Reversi")

    while True:
        playGame()
        if playersAreBored():
            break


def playersAreBored():
    while True:
        areTheyBored = input("Are you bored yet [y/n]? ").lower()
        if areTheyBored == "y":
            print("Bye then...")
            return True
        if areTheyBored == "n":
            clearScreen()
            print("Excellent!  Another game...")
            return False
        print("Huh? ")


def getPlayers():
    print("Which game mode do you wish to use?")
    choices = [
        ("A", "Computer vs Computer", getAiVsAiOpponents()),
        ("B", "Human vs Human", getHumanVsHumanOpponents()),
        ("C", "Computer vs Human", getAiVsHumanOpponents())
    ]
    for choice in choices:
        print("{0} {1}".format(choice[0], choice[1]))
    while True:
        gameMode = input(": ").upper()
        for choice in choices:
            if choice[0] == gameMode:
                return choice[2]


def getHumanVsHumanOpponents():
    return (
        HumanPlayer(1, gameBoard),
        HumanPlayer(2, gameBoard)
    )


def getAiVsHumanOpponents():
    return (
        AIPlayer(1, gameBoard),
        HumanPlayer(2, gameBoard)
    )


def getAiVsAiOpponents():
    p1 = AIPlayer(1, gameBoard)
    p2 = AIPlayer(2, gameBoard)
    return (p1, p2)


def clearScreen():
    print("\n" * 3)


def gameIsOver():
    if len(gameBoard.moves) > 0:
        return False

    if gameBoard.score[0] == gameBoard.score[1]:
        print("It's a draw.  How dull.")
        return True

    if gameBoard.score[0] > gameBoard.score[1]:
        winner = 1
    else:
        winner = 2

    print("Player {0} has won!".format(gameBoard.getPlayerCharacter(winner)))
    return True


def playGame():
    global gameBoard
    gameBoard = GameBoard()
    players = getPlayers()

    playerNumber = 1
    while True:
        gameBoard.showScore()
        gameBoard.drawBoard(assessForPlayer=playerNumber)

        if gameIsOver():
            break

        print("Player {0}'s turn.".format(gameBoard.getPlayerCharacter(playerNumber)))
        players[playerNumber - 1].makeMove()

        playerNumber = gameBoard.opponentNumber(playerNumber)


main()
