import random

SUIT_LIST = ["♠", "♥", "♦", "♣"]
RANK_DICTIONARY = {
    "A": 11,  # Special case - sometimes this can be 1
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def create_card_deck():
    card_deck = []
    for suit in SUIT_LIST:
        for rank in RANK_DICTIONARY:
            card = rank + suit
            card_deck.append(card)
    return card_deck


def shuffle_card_deck(card_deck):
    random.shuffle(card_deck)
    return card_deck


def draw_card(card_deck):
    card = card_deck.pop()
    return card


def draw_hand(card_deck):
    return [
        draw_card(card_deck),
        draw_card(card_deck)
    ]


def get_card_rank(card):
    suit_string = ''.join(SUIT_LIST)
    return card.strip(suit_string)


def evaluate_hand(hand_of_cards):
    hand_value = 0
    ace_is_present = False

    for card in hand_of_cards:
        rank = get_card_rank(card)
        card_value = RANK_DICTIONARY[rank]
        hand_value += card_value
        if card_value == 11:
            ace_is_present = True

    player_is_bust = is_player_bust(hand_value)
    if ace_is_present and player_is_bust:
        hand_value -= 10

    return hand_value


def is_player_bust(hand_value):
    return hand_value > 21


def get_players_choice(choice_description, valid_choice_list):
    while True:
        choice = input(choice_description).upper()
        if choice in valid_choice_list:
            return choice
        print("Invalid choice")


def get_players_move(card_deck, players_hand):
    while True:
        print(players_hand)
        players_hand_value = evaluate_hand(players_hand)

        if players_hand_value >= 21:
            break

        players_choice = get_players_choice("[H]it or [S]tand? ", ["H", "S"])
        if players_choice == "S":
            break

        another_card = draw_card(card_deck)
        players_hand.append(another_card)
    return players_hand_value


def check_for_blackjack(hand_of_cards):
    hand_value = evaluate_hand(hand_of_cards)
    if hand_value != 21:
        return

    if len(hand_of_cards) > 2:
        return

    for card in hand_of_cards:
        rank = get_card_rank(card)
        card_value = RANK_DICTIONARY[rank]
        if card_value == 11:
            print("Blackjack!")


def play_round_of_cards():
    card_deck = create_card_deck()
    card_deck = shuffle_card_deck(card_deck)
    dealers_hand = draw_hand(card_deck)
    players_hand = draw_hand(card_deck)
    players_hand_value = get_players_move(card_deck, players_hand)
    dealers_hand_value = evaluate_hand(dealers_hand)
    print("I have:", dealers_hand)
    if is_player_bust(players_hand_value):
        print("You are bust")
    elif players_hand_value > dealers_hand_value:
        print("You win")
        check_for_blackjack(players_hand)
    elif players_hand_value < dealers_hand_value:
        print("I win")
        check_for_blackjack(dealers_hand)
    else:
        print("draw")


def main():
    play_again = True
    while play_again:
        play_round_of_cards()
        play_again = get_players_choice("Play [A]gain or [Q]uit?", ["A", "Q"])


if __name__ == '__main__':
    main()
