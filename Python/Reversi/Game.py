from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer
from Graphics import Graphics


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


def get_players():
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
        HumanPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def getAiVsHumanOpponents():
    return (
        AIPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def getAiVsAiOpponents():
    p1 = AIPlayer(1, game_board)
    p2 = AIPlayer(2, game_board)
    return (p1, p2)


def clearScreen():
    print("\n" * 3)


def game_is_over():
    if len(game_board.moves) > 0:
        return False

    graphics.draw_board()
    graphics.update()

    if game_board.score[0] == game_board.score[1]:
        print("It's a draw.  How dull.")
        graphics.display_message("It's a draw.  How dull.")
        return True

    if game_board.score[0] > game_board.score[1]:
        winner = 1
    else:
        winner = 2

    print("Player {0} has won!".format(game_board.get_player_character(winner)))
    graphics.display_message("Player {0} has won!".format(winner))
    return True


def playGame():
    global game_board
    global graphics

    game_board = GameBoard()
    players = get_players()
    graphics = Graphics((300, 300), game_board)

    player_number = 1
    while True:
        game_board.show_score()
        game_board.draw_ascii_board(assess_for_player=player_number)

        if game_is_over():
            break

        print("Player {0}'s turn.".format(game_board.get_player_character(player_number)))

        players[player_number - 1].make_move(graphics)

        player_number = game_board.opponent_number(player_number)

    graphics.close()

main()
