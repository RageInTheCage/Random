##Imports##


import random


##Loading and Saving##


def recipes(itemWanted):
    recipeForItemWanted = []
    recipesForItems = readFile("recipes.txt")
    recipesForItems = [items.strip() for items in recipesForItems]
    nameOfRecipe = recipesForItems.index(itemWanted + "-")
    itemToSearch = nameOfRecipe + 2
    amountOfItems = int(recipesForItems[nameOfRecipe + 1])
    for item in recipesForItems:
        if "-" in recipesForItems[itemToSearch]:
            break
        else:
            recipeForItemWanted.append(recipesForItems[itemToSearch])
            itemToSearch += 1
    return recipeForItemWanted, amountOfItems


def readFile(file):
    readFromFile = open(file, "r")
    lines = readFromFile.readlines()
    lines = [each.strip() for each in lines]
    readFromFile.close()
    return lines


def saveGame(inventory, money):
    print("Saving...")
    saveItem = open("inventory.txt", "w")
    saveItem.write("Money-\n{0}\nItems-\n".format(money))
    for each in inventory:
        saveItem.write(each + "\n")
    saveItem.close()
    print("Saved.")


def loadData():
    print("Loading saves...")
    inventory = readFile("inventory.txt")
    money = inventory[1]
    inventory = removeItem(inventory, "Money-")
    inventory = removeItem(inventory, "Items-")
    inventory = removeItem(inventory, money)
    print("Saves loaded.")
    return inventory, money


def resetGame():
    print("Resetting...")
    inventory = []
    print("Reset.")
    saveGame(inventory, 0)


##Starting Menu##


def randomTip():
    tips = ["When you have reset the game, you need to open the game with the load game option.", "When crafting, if you want to cancel, just write 0 as the quantity.", "Be sure to check out the store to see if there are any new items.", "Artisan items can be usually sold for more than there ingredients.", "Upgrade your skills to make higher quality items", "Some items might be more expensive but are sometimes less appealing to the public.", "Remember to upgrade your warehouse to increase your inventory size.", "Some people will prefer to trade than by or sell items", "Items will increase and decrease in value so make sure you by items when they are cheap and sell when they are expensive."]
    tip = tips[random.randint(0, len(tips) - 1)]
    return tip


def startMenu():
    while True:
        tip = randomTip()
        menuChoice = input("-GAME-\n\nMenu:\n\n-Load Game(A)\n-Start New Game(B)\n-Options(C)\n-Quit(D)\nTip: {0}\n\n:  ".format(tip)).upper()
        if menuChoice == "A":
            character()
        elif menuChoice == "B":
            newGameChoice = input("Are you sure you want to start a new game?\nThis will overwrite your old save\n(Y or N)\n\n:  ").upper()
            if newGameChoice == "Y":
                resetGame()
                print("A new game has been created.")
            elif newGameChoice == "N":
                print()
            else:
                print("{0} is not an option.".format(newGameChoice.capitalize()))
        elif menuChoice == "C":
            options()
        elif menuChoice == "D":
            quit()


##Inventory Management##


def addItem(inventory, itemToAdd):
    inventory.append(itemToAdd)
    return inventory


def removeItem(inventory, itemToRemove):
    index = inventory.index(itemToRemove)
    inventory.pop(index)
    return inventory


def printInventory(inventory):
    prevItem = None
    inventory.sort()
    for item in inventory:
        if prevItem == item:
            pass
        else:
            numberOfItems = inventory.count(item)
            print("{0} x {1}".format(item, str(numberOfItems)))
        prevItem = item





##Crafting##


def craftItem(itemsWanted, recipeForItems, amountOfItemsMadeSeperatly, numberOfItemsWanted, inventory):
    print(amountOfItemsMadeSeperatly)
    for x in range(0, numberOfItemsWanted):
        for items in recipeForItems:
            removeItem(inventory, items)
        for x in range(0, amountOfItemsMadeSeperatly):
            addItem(inventory, itemsWanted)
    return inventory


def craftingMenu(inventory):
    while True:
        wantedItem = input("\nWhat do you want to craft?\n:  ").title()
        if wantedItem + "-" not in open("recipes.txt").read():
            print("{0} is not an item. Please try again.".format((wantedItem.lower()).capitalize()))
            continue
        break
    while True:
        amountOfItemsWanted = input("\nHow many of them do you want?\n:  ")
        try:
            amountOfItemsWanted = int(amountOfItemsWanted)
        except ValueError:
            print("{0} is not a number. Please try again.".format((amountOfItemsWanted.lower()).capitalize()))
            continue
        recipeForItems, amountOfItemsMadeSeperatly = recipes(wantedItem)
        try:
            testInventory = craftItem(wantedItem, recipeForItems, amountOfItemsMadeSeperatly, amountOfItemsWanted, inventory)
            break
        except ValueError:
            print("You don\'t have enough items to make {0} {1}.".format(str(amountOfItemsWanted), wantedItem.lower()))
            continue
    inventory = testInventory
    printInventory(inventory)
    return inventory


##Character##


def warehouse(inventory):
    print("-Bank-\n{0}\n-Items-")
    printInventory(inventory)
    input()


def character():
    inventory, money = loadData()
    while True:
        characterChoice = input("-Character-\n\nMenu:\n-Craft Items(A)\n-Sell Items(B)\n-Warehouse(C)\n-Shop(D)\n-Back(E)\n\n:  ").upper()
        if characterChoice == "A":
            inventory = craftingMenu(inventory)
        elif characterChoice == "B":
            inventory = itemSeller(inventory)
        elif characterChoice == "C":
            warehouse(inventory)
        elif characterChoice == "D":
            print("Not yet")
        elif characterChoice == "E":
            saveGame(inventory, money)
            return inventory
        else:
            print("{0} is not an option. Please try again.".format((characterChoice.lower()).capitalize()))


##W.I.P. / Misc##


def itemSeller(testInventory):
    while True:
        print("-Sell Items-\n\nWhat item do you want to sell?")
        printInventory(testInventory)
        itemToSell = input(":  ").title()
        try:
            print(testInventory.index(itemToSell))
            break
        except ValueError:
            continue
    while True:
        amountOfItems = int(input("What quantity of {0} would you like to sell?\n:  ".format(itemToSell)))
        try:
            print(testInventory)
            for x in range(0, amountOfItems):
                testInventory = removeItem(testInventory, itemToSell)
            break
        except ValueError:
            print("You don't have {0} {1}.".format(amountOfItems, itemToSell))
            continue
    inventory = testInventory
    return inventory


def options():
    print("Not yet\n")


##Start Up##


startMenu()
