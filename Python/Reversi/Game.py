import pygame

from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer
from Graphics import Graphics


def main():
    game_board = GameBoard()
    graphics = Graphics((800, 800), game_board)

    while True:
        play_game(game_board, graphics)

        if players_are_bored(graphics):
            break

        game_board = GameBoard()
        graphics.game_board = game_board


def play_game(game_board, graphics):
    game_board.players = get_players(game_board, graphics)

    player = game_board.players[0]
    while True:
        game_board.show_score(game_board.players)
        game_board.draw_ascii_board(assess_for_player=player.number)

        if game_is_over(game_board, graphics):
            break

        print("Player {0}'s turn.".format(player.character))
        player.make_move(graphics)

        player = player.opponent


def get_players(game_board, graphics):
    if graphics.ask("Play against me?") == pygame.K_y:
        return get_ai_vs_human_opponents(game_board)

    if graphics.ask("Someone else?") == pygame.K_y:
        return get_human_vs_human_opponents(game_board)

    graphics.say("Fine, I'll play me!")
    return get_ai_vs_ai_opponents(game_board)


def get_human_vs_human_opponents(game_board):
    return (
        HumanPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_ai_vs_human_opponents(game_board):
    return (
        AIPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_ai_vs_ai_opponents(game_board):
    p_1 = AIPlayer(1, game_board)
    p_2 = AIPlayer(2, game_board)
    return p_1, p_2


def game_is_over(game_board, graphics):
    if len(game_board.moves) > 0:
        return False

    graphics.draw_board()
    graphics.update()

    score_difference = game_board.players[0].score - game_board.players[1].score

    if score_difference == 0:
        message = "It's a draw.  How dull."
    else:
        if score_difference > 0:
            winner = game_board.players[0]
        else:
            winner = game_board.players[1]
        message = "Player {0} has won!".format(winner.name)

    print(message)
    graphics.say(message)
    return True


def players_are_bored(graphics):
    return graphics.ask("Another game?") == pygame.K_n


main()
