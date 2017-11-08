import shelve
import random

#apps needs work (a lot!)

def apps(score):
    while True:
        count = 0
        Applications = ["Number guessing game"]
        Applications.sort()
        print("Applications\n")
        appNumber = 1
        for A in (Applications):
            print("-" + A + "(" + str(appNumber) + ")")
            appNumber += 1
        chooseApp = input(":  ")
        try:
            chooseAppNumber = int(chooseApp)
        except ValueError:
            print(chooseApp.capitalize() + " is not a number.")

        appNumber -= 1

        if chooseAppNumber > appNumber or chooseAppNumber < appNumber:
            print(str(chooseApp) + " is not on the list")
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
                print("not yet")



def shop():
    print("Sorry but the shop is not currently open.")
    shopStock = open("shopStock.txt", "r")
    print(shopStock.read())
    byItem = input(":  ").upper()
    something = "(" + byItem + ")"
    #do stuff here
    with open("shopStock.txt") as f:
        stock = f.readlines()
    if something in open("shopStock.txt").read():
        print()
    else:
        print("damn")


def numberGuessingGame():
    randomNumber = random.randint(1000,9999)

    while True:
        difficulty = input("Number guessing game!\nChoose your dificulty\n-Easy(A)-20 tries to guess the 4 didit number\n-Hard(B)-10 tries to guess the 4 digit number. 4x all points.\n:  ").upper()

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
                choice = input("Guess my four diget number in " + userFriendly + " guesses!\n:  ")
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
            shop()
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
print("Save files opend.")

main(score)



     
