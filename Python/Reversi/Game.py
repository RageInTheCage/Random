import pygame

from AIPlayer import AIPlayer
from GameBoard import GameBoard
from Graphics import Graphics
from HumanPlayer import HumanPlayer


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
    graphics.set_board_pieces()
    game_board.players = get_players(game_board, graphics)

    player = game_board.players[0]
    zero_move_count = 0
    while True:
        game_board.show_score(game_board.players)
        graphics.set_board_pieces()
        graphics.score_overlay.refresh(game_board.players)

        game_board.draw_ascii_board(assess_for_player=player.number)

        if len(game_board.moves) == 0:
            zero_move_count += 1
            if zero_move_count == 1:
                graphics.say("{0} cannot move.".format(player.name))
            elif game_is_over(game_board, graphics):
                break
        else:
            zero_move_count = 0
            print("{0}'s turn.".format(player.name))
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
    delay = 0
    p_1 = AIPlayer(1, game_board, delay)
    p_2 = AIPlayer(2, game_board, delay)
    return p_1, p_2


def game_is_over(game_board, graphics):
    score_difference = game_board.players[0].score - game_board.players[1].score

    if score_difference == 0:
        message = "It's a draw.  How dull."
    else:
        if score_difference > 0:
            winner = game_board.players[0]
        else:
            winner = game_board.players[1]
        message = "{0} has won!".format(winner.name)

    graphics.score_overlay.show_winner(message, game_board.players)
    graphics.say(message)
    graphics.animate_winning_pieces(winner.number)
    return True


def players_are_bored(graphics):
    if graphics.ask("Another game?") == pygame.K_y:
        return False
    graphics.say("Okay, bye then...")
    graphics.wait_for_animation(frame_count=40)
    return True


main()
