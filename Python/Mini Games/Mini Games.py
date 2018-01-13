import shelve
import random

def BlackJack():
    print("->---<$>--<BlackJack>--<$>---<-")
    choiceLoop = 0
    while choiceLoop<1:
        print("\n-Rules(A)\n-I already know how to play(B)\n-Back(Back)")
        choice = input(":  ").upper()
        if choice == "A":
            introToBlackJack()
        elif choice == "B":
            results = playBlackJack()
            if results == True:
                return 5
            if results == False:
                return -5
            if results == None:
                return 0
        elif choice == "BACK":
            return
        else:
            print(choice.capitalize() , " is not an option. Try again.")

def introToBlackJack():
    print("Noooooooooooooo!")
    return

def playBlackJack():
    dealerHasMissed = False
    playerHasMissed = False
    score = 0
    dealerScore = 0
    cardTaken = False
    while True:
        if playerHasMissed == False:
            Rank = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
            Set = (" of Diamonds", " of Spades", " of Clubs", " of Hearts")
            rank = random.choice(Rank)
            if rank == "Ace":
                score += 1
            elif rank == "Jack":
                score += 10
            elif rank == "Queen":
                score += 10
            elif rank == "King":
                score += 10
            else:
                score += int(rank)
            cards = (rank + random.choice(Set))
            if cardTaken == False:
                print("your first card is " + cards)
                print("Your current score is " + str(score))
                cardTaken = True
                break
            elif cardTaken == True:
                print("Your next card is " + cards)
                print("Your current score is " + str(score))
                break
            if score == dealerScore and score == 21:
                print("We drew!\n")
                return None
            if score == 21:
                print("You win!\n")
                if dealerScore > 21:
                    print("The dealer is bust!\n")
                    return True
                else:
                    return True
            if score > 21:
                print("Your bust!\n")
                return False
        if dealerScore > 21:
            print("The dealer is bust!\n")
            return True
        if playerHasMissed == False:
            while True:
                askForMiss = input("do you want to hit(H) or miss(M)?\n:  ")
                if askForMiss == "H":
                    print("O.K.")
                    break
                elif askForMiss == "M":
                    playerHasMissed = True
                    print("You have missed.\nYou had a score of " + str(score))
                    break
                else:
                    print(askForMiss.capitalize() + " is not an option.")

        if dealerHasMissed == False:
            dealerScore += random.randint(1, 12)
            dealerMiss = random.randint(0, 3)
            if dealerScore == 21:
                dealerMiss = 0
            if dealerMiss == 0:
                print("The dealer has missed.\nHe had a score of " + str(dealerScore))
                dealerHasMissed = True
                if dealerScore == score and playerHasMissed == True:
                    print("You Drew!")
                    return None
                elif dealerScore < score and playerHasMissed == True:
                    print("You win!")
                    return True
                elif dealerScore > score and playerHasMissed == True:
                    print("The dealer has won")
                    return False
            else:
                print("The dealer has hit")


def apps(score):
    while True:
        while True:
            with open("boughtApps.txt") as f:
                Applications = f.readlines()
                Applications = [x.strip() for x in Applications]
                Applications.sort()
            Applications.sort()
            print("Applications\n")
            appNumber = 1
            for A in Applications:
                print("-" + A + "(" + str(appNumber) + ")")
                appNumber += 1
            print("-Back(Quit)")
            chooseApp = input(":  ").upper()
            if chooseApp == "QUIT":
                return 0
            try:
                chooseAppNumber = int(chooseApp)
                if chooseAppNumber == 0:
                    print("0 is not on the list\n")
                else:
                    break
            except ValueError:
                print(chooseApp.capitalize() + " is not a number.")

        appNumber -= 1

        if chooseAppNumber > appNumber or chooseAppNumber < 0:
            print(str(chooseApp) + " is not on the list.")
        else:
            chooseAppNumber -= 1
            chosenApp = Applications[chooseAppNumber]
            if chosenApp == "Number guessing game":

                while True:
                    score = 0
                    gameScore = numberGuessingGame()

                    if gameScore == -1:
                        print("-1 point!")
                        score -= 1
                    elif gameScore == 1:
                        print("+1 point")
                        score += 1
                    else:
                        print("+" + str(gameScore) + " points")
                        score += gameScore

                    choice = input("Again?\n(Y or N)\n:  ").upper()

                    if choice == "Y":
                        input("Great!")
                    elif choice == "N":
                        print("good bye!")
                        return score
                    else:
                        print(choice + " is not an option.")
            elif chosenApp == "Blackjack":

                while True:
                    score = 0
                    gameScore = BlackJack()
                    if gameScore == -5:
                        print("-5 points")
                        score -= 5
                    elif gameScore == 5:
                        print("+5 points")
                        score += 5
                    else:
                        print("+0 points")

                    choice = input("Again?\n(Y or N)\n:  ").upper()

                    if choice == "Y":
                        input("Great!")
                    elif choice == "N":
                        print("good bye!")
                        return score
                    else:
                        print(choice + " is not an option.")


def shop(score):
    boughtMessage = "Great! Your purchase will be ready in your apps."
    while True:
        with open("shopStock.txt") as f:
            stock = f.readlines()
            stock = [x.strip() for x in stock]
            stock.sort()
        while True:

            appNumber = 1

            for S in stock:
                print("-" + S + "(" + str(appNumber) + ")")
                appNumber += 1
            print("-Back(Quit)")
            chooseApp = input(":  ").upper()
            if chooseApp == "QUIT":
                return 0
            try:
                chooseAppNumber = int(chooseApp)
                if chooseAppNumber == 0:
                    print("0 is not on the list\n")
                else:
                    break
            except ValueError:
                print(chooseApp.capitalize() + " is not a number.")

        appNumber -= 1

        if chooseAppNumber > appNumber or chooseAppNumber < 0:
            print(str(chooseApp) + " is not on the list.")
        else:
            chooseAppNumber -= 1
            chosenApp = stock[chooseAppNumber]
            if chosenApp == "Blackjack:             20 points":
                if score >= 20:
                    print(boughtMessage)
                    boughtApps = open("boughtApps.txt", "a")

                    boughtApps.write("Blackjack\n")

                    readShopFiles = open("shopStock.txt", "r")
                    linesInFile = readShopFiles.readlines()
                    readShopFiles.close()
                    writeShopFiles = open("shopStock.txt", "w")
                    for line in linesInFile:
                        if line != "Blackjack:             20 points" + "\n":
                            writeShopFiles.write(line)
                    writeShopFiles.close()

                    return 20
                else:
                    print("Sorry but Blackjack is too expensive for you to afford. try some other games to save up points.")
            if chosenApp == "Hangman:               20 points":
                if score >= 20:
                    print(boughtMessage)
                    boughtApps = open("boughtApps.txt", "a")

                    boughtApps.write("Hangman\n")

                    readShopFiles = open("shopStock.txt", "r")
                    linesInFile = readShopFiles.readlines()
                    readShopFiles.close()
                    writeShopFiles = open("shopStock.txt", "w")
                    for line in linesInFile:
                        if line != "Hangman:               20 points" + "\n":
                            writeShopFiles.write(line)
                    writeShopFiles.close()

                    return 20
                else:
                    print("Sorry but Hangman is too expensive for you to afford. try some other games to save up points.")
            if chosenApp == "Noughts and crosses:   30 points":
                if score >= 30:
                    print(boughtMessage)
                    boughtApps = open("boughtApps.txt", "a")

                    boughtApps.write("Noughts and crosses\n")
                    readShopFiles = open("shopStock.txt", "r")
                    linesInFile = readShopFiles.readlines()
                    readShopFiles.close()
                    writeShopFiles = open("shopStock.txt", "w")
                    for line in linesInFile:
                        if line != "Noughts and crosses:   30 points" + "\n":
                            writeShopFiles.write(line)
                    writeShopFiles.close()

                    return 30
                else:
                    print("Sorry but Noughts and crosses is too expensive for you to afford. try some other games to save up points.")
            if chosenApp == "Mine blower:           50 points":
                if score >= 50:
                    print(boughtMessage)
                    boughtApps = open("boughtApps.txt", "a")

                    boughtApps.write("Mine blower\n")
                    readShopFiles = open("shopStock.txt", "r")
                    linesInFile = readShopFiles.readlines()
                    readShopFiles.close()
                    writeShopFiles = open("shopStock.txt", "w")
                    for line in linesInFile:
                        if line != "Mine blower:           50 points" + "\n":
                            writeShopFiles.write(line)
                    writeShopFiles.close()

                    return 50
                else:
                    print("Sorry but Mine Blower is too expensive for you to afford. try some other games to save up points.")

            print("The app you have chosen is not in stock and will probably never be. Sorry.\n")



def numberGuessingGame():
    randomNumber = random.randint(1000,9999)

    while True:
        difficulty = input("Number guessing game!\nChoose your difficulty\n-Easy(A)-20 tries to guess the 4 digit number\n-Hard(B)-10 tries to guess the 4 digit number. 4x all points.\n:  ").upper()

        if difficulty == "A":
            guessesLeft = 20
        elif difficulty == "B":
            guessesLeft = 10
        else:
            (difficulty.capitalize() + " is not an option.")
            print()

        while True:

            while True:
                userFriendly = str(guessesLeft)
                choice = input("Guess my four digit number in " + userFriendly + " guesses!\n:  ")
                print("")

                try:
                    value = float(choice)
                    break
                except ValueError:
                    print("That's not a number\n")

            if difficulty == "A":
                gameScore = guessesLeft
            else:
                gameScore = guessesLeft * 4
                    
            if difficulty == "A":
                guessesTaken = 20 - guessesLeft
            else:
                guessesTaken = 10 - guessesLeft
                    
            if value == randomNumber and gameScore == 20 or value == randomNumber and gameScore == 40 and difficulty == "B":
                print("Well done! You got it first try!")
                return gameScore * 2
            
            if value == randomNumber:
                print("Well done! You got it in " + str(guessesTaken) + " tries!")
                return gameScore
            
            if guessesLeft == 0:
                print("Oh no! You lost! better luck next time!")
                return -1
            
            if value > randomNumber:
                print("This number is too high.")
                
            if value < randomNumber:
                print("This number is too low.")

            guessesLeft -= 1


def main(score):

    while True:
        userFriendlyScore = str(score)

        print("Menu:\n\n-Apps(A)\n-Shop(B)\n-Reset all save data(C)\n-Save and quit(Quit)\n\nYou have " + userFriendlyScore + " points.")
        menu = input("\n:  ").upper()

        if menu == "A":
            score += apps(score)
                
        elif menu == "B":
            score -= shop(score)
            d = shelve.open('score.txt')
            d['score'] = score
            d.close()

        elif menu == "C":

            while True:
                reset = input("Are you sure you want to reset?\n(Y or N)\n:  ").upper()

                if reset == "N":
                    break
                elif reset == "Y":
                    password = input("\nEnter password\n:  ")

                    if password == "FEAT":
                        print("Resetting all data...")
                        score = 0
                        resetShopStock = open("shopStock.txt", "w")
                        resetShopStock.write("Blackjack:             20 points\nHangman:               20 points\nNoughts and crosses:   30 points\nMine blower:           50 points\n")
                        resetShopStock.close()
                        resetBoughtApps = open("boughtApps.txt", "w")
                        resetBoughtApps.write("Number guessing game\n")
                        resetBoughtApps.close()
                        d = shelve.open('score.txt')
                        d['score'] = score
                        d.close()
                        print("All data reset")
                        break
                    else:
                        quit()
                else:
                    print(reset.capitalize() + " is not an option.")
                    
        elif menu == "QUIT":
            print("Saving...")
            d = shelve.open('score.txt')   
            d['score'] = score           
            d.close()
            print("Points saved!")
            quit()
        else:
            print(menu.capitalize() + " is not an option.")
        
    
print("Opening save files...")
d = shelve.open('score.txt')
score = d['score']
print("Save files open'd.")

score += 200

main(score)
