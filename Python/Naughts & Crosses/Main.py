from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from GameBoard import GameBoard


def main():
    clear_screen()
    print('Welcome to our Naughts & crosses game.  Do you feel lucky punk?')

    while True:
        play_game()
        if players_are_bored():
            break


def play_game():
    global game_board
    game_board = GameBoard(3, 3)
    players = get_players()

    player_number = 1
    for move_number in range(1, game_board.width * game_board.height):
        print('Player {0}''s turn.'.format(game_board.get_player_letter(player_number)))

        game_board.draw_board()
        players[player_number - 1].makeMove()

        if game_board.player_has_won(player_number):
            finish_game(player_number)
            return

        clear_screen()
        player_number = 3 - player_number

    print("It's a draw - how dull.")


def get_players():
    print("Which game mode do you wish to use?")
    choices = [('A', 'Computer vs Computer', get_ai_vs_ai_opponents()),
               ('B', 'Human vs Human', get_human_vs_human_opponents()),
               ('C', 'Computer vs Human', get_ai_vs_human_opponents())]
    for choice in choices:
        print('{0} {1}'.format(choice[0], choice[1]))
    while True:
        game_mode = input(': ').upper()
        for choice in choices:
            if choice[0] == game_mode:
                return choice[2]


def get_ai_vs_human_opponents():
    return (
        AIPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_human_vs_human_opponents():
    return (
        HumanPlayer(1, game_board),
        HumanPlayer(2, game_board)
    )


def get_ai_vs_ai_opponents():
    p1 = AIPlayer(1, game_board)
    p2 = AIPlayer(2, game_board)
    return p1, p2


def finish_game(winning_player):
    clear_screen()
    print(f"Well done player {game_board.get_player_letter(winning_player)}, you won!")
    game_board.draw_board()


def clear_screen():
    print('\n' * 3)


def players_are_bored():
    while True:
        are_they_bored = input('Are you bored yet [y/n]? ').lower()
        if are_they_bored == 'y':
            print('Charming!  Bye then...')
            return True
        if are_they_bored == 'n':
            clear_screen()
            print('Excellent!  Another game, goody...')
            return False
        print('Huh? ')


main()
