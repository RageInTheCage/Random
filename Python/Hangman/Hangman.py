import random


def diplayHangman(level_of_death):
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
        print("  |         0")
        print("  |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 6:
        print("   _________")
        print("  |         |")
        print("  |         0")
        print("  |         |")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 7:
        print("   _________")
        print("  |         |")
        print("  |         0")
        print("  |         |\\")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 8:
        print("   _________")
        print("  |         |")
        print("  |         0")
        print("  |        /|\\")
        print("  |")
        print(" /|\\")
        print("/_|_\\_________")

    elif level_of_death == 9:
        print("   _________")
        print("  |         |")
        print("  |         0")
        print("  |        /|\\")
        print("  |        /")
        print(" /|\\")
        print("/_|_\\_________")
    else:
        print("   _________")
        print("  |         |")
        print("  |         0")
        print("  |        /|\\")
        print("  |        / \\")
        print(" /|\\")
        print("/_|_\\_________")


def swapOutLetters(lettersGuessed, guessedLetter, word):
    correctAnswer = False
    for character in range(0, len(word)):
        letter = word[character]
        if letter == guessedLetter:
            lettersGuessed = lettersGuessed[:character] + letter + lettersGuessed[character + 1:]
            correctAnswer = True
    return lettersGuessed, correctAnswer


def inputSingleLetter():
    while True:
        letter = input(":  ").upper()
        if len(letter) == 1:
            return letter
        print("Expected a single character")

def inputLetter(lettersGuessed):
    print("Guess a letter!")
    while True:
        guessedLetter = inputSingleLetter()
        if lettersGuessed.count(guessedLetter) == 0:
            return guessedLetter
        print("You have already chosen " + guessedLetter + " as a letter.")


def showLetters(lettersGuessed):
    for letter in lettersGuessed:
        print(letter, end=' ')


def game():
    dictionary = ["PYTHON", "SCRIPT", "CODE", "COMMAND", "PRINT"]
    random.shuffle(dictionary)
    word = dictionary[0]
    levelOfDeath = 0
    print(word)
    lettersGuessed = '_' * len(word)

    while True:
        showLetters(lettersGuessed)
        guessedLetter = inputLetter(lettersGuessed)
        lettersGuessed, isCorrect = swapOutLetters(lettersGuessed, guessedLetter, word)

        if isCorrect:
            print("Yay!")
            if lettersGuessed == word:
                print("Well done my friend!")
                return
        else:
            levelOfDeath += 1
            print("*Evil laughter*")
            diplayHangman(levelOfDeath)

            if levelOfDeath == 10:
                print("*Even more evil laughter than before*")
                return


def userIsBored():
    while True:
        print ("Another game (Y/N)?")
        reply = inputSingleLetter()
        if reply == "N" or reply == "Y":
            return reply == "N"


while True:
    game()
    if userIsBored():
        break