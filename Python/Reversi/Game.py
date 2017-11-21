import pygame

from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer
from Graphics import Graphics


def main():
    while True:
        play_game()
        if players_are_bored():
            break


def players_are_bored():
    while True:
        areTheyBored = input("Are you bored yet [y/n]? ").lower()
        if areTheyBored == "y":
            print("Bye then...")
            return True
        if areTheyBored == "n":
            print("Excellent!  Another game...")
            return False
        print("Huh? ")


def get_players():
    if graphics.ask("Play against me?") == pygame.K_y:
        return get_ai_vs_human_opponents()

    if graphics.ask("Someone else?") == pygame.K_y:
        return get_human_vs_human_opponents()

    return get_ai_vs_ai_opponents()


def get_human_vs_human_opponents():
    return (
        HumanPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_ai_vs_human_opponents():
    return (
        AIPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_ai_vs_ai_opponents():
    p_1 = AIPlayer(1, game_board)
    p_2 = AIPlayer(2, game_board)
    return (p_1, p_2)


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


def play_game():
    global game_board
    global graphics

    game_board = GameBoard()
    graphics = Graphics((400, 400), game_board)
    players = get_players()

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
