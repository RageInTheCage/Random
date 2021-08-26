import random


def display_hangman(level_of_death):
    print(level_of_death)
    if level_of_death == 1:
        print("\n\n\n\n\n")
        print(" _____________")

    elif level_of_death == 2:
        print("   ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 3:
        print("   _________")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 4:
        print("   _________")
        print("  |         |")
        print("  |         |")
        print("  |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 5:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 6:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |         |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 7:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |         |\\")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 8:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |        /|\\")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 9:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |        /|\\")
        print("  |        /")
        print(" /|\\")
        print("/_|_\\_________")
    else:
        print("   _________")
        print("  |         |")
        print("  |         O")
        print("  |        /|\\")
        print("  |        / \\")
        print(" /|\\")
        print("/_|_\\_________")


def swap_out_letters(letters_guessed, guessed_letter, word):
    is_correct_answer = False
    for character in range(0, len(word)):
        letter = word[character]
        if letter == guessed_letter:
            letters_guessed = letters_guessed[:character] + letter + letters_guessed[character + 1:]
            is_correct_answer = True
    return letters_guessed, is_correct_answer


def input_single_letter():
    while True:
        letter = input(":  ").upper()
        if len(letter) == 1:
            return letter
        print("Expected a single character")


def input_letter(letters_already_guessed):
    print("Guess a letter!")
    while True:
        guessed_letter = input_single_letter()

        if guessed_letter not in letters_already_guessed:
            letters_already_guessed.append(guessed_letter)
            return guessed_letter

        print(f"You have already chosen {guessed_letter} as a letter.")


def show_letters(letters_guessed):
    for letter in letters_guessed:
        print(letter, end=' ')


def get_hangman_dictionary():
    dictionary = ["PYTHON", "SCRIPT", "CODE", "COMMAND", "PRINT"]
    random.shuffle(dictionary)

    return dictionary


def get_word(hangman_dictionary):
    if not len(hangman_dictionary):
        hangman_dictionary = get_hangman_dictionary()

    return hangman_dictionary.pop()


def play_game():
    word = get_word(hangman_dictionary)
    level_of_death = 0
    word_placeholder = '_' * len(word)
    show_letters(word_placeholder)
    letters_already_guessed = []

    while True:
        guessed_letter = input_letter(letters_already_guessed)
        word_placeholder, is_correct_answer = swap_out_letters(word_placeholder, guessed_letter, word)
        show_letters(word_placeholder)

        if is_correct_answer:
            print("Yay!")
            if word_placeholder == word:
                print("Well done my friend, you survived the hangman's noose!")
                return
            continue

        level_of_death += 1
        print("Wrong")
        display_hangman(level_of_death)

        if level_of_death == 10:
            print(f'You\'re hung!  The word was "{word}"')
            return


def user_is_bored():
    while True:
        print("Another game (Y/N)?")
        reply = input_single_letter()
        if reply == "N" or reply == "Y":
            return reply == "N"


while True:
    hangman_dictionary = get_hangman_dictionary()
    play_game()
    if user_is_bored():
        break
