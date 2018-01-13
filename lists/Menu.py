def main():
    newGameMenu = ["-1 player game", "-2 player game"]
    loadGameMenu = ["Happyland 21.11.2017", "Large City 17.4.2015", "Hardcore 05.03.2016"]
    optionsMenu = ["Audio", "Video"]
    quitOption = ["Yes I want to quit"]
    mainMenuItems = [newGameMenu, loadGameMenu, optionsMenu, quitOption]
    mainMenuItemNames = ["New Game", "Load Game", "Options", "Quit"]
    while True:
        userSelection = showMenu("Main Menu", mainMenuItemNames, mainMenuItems, False)
        if userSelection == -1:
            continue
        menuName = mainMenuItemNames[userSelection]
        menuItemNames = mainMenuItems[userSelection]
        userSelection = showMenu(menuName, menuItemNames, mainMenuItems)
        runMenuCommand(menuItemNames, userSelection)


def runMenuCommand(menuItemNames, userSelection):
    if userSelection == -1:
        print("You chose back")
        return
    else:
        print("You chose {0}".format(menuItemNames[userSelection]))
    if menuItemNames[userSelection] == "Yes I want to quit":
        quit()


def showMenu(menuName, menuItemNames, menuItems, showBackItem = True):
    menuNum = 0
    allMenuItemNames = list(menuItemNames)
    backIndex = None
    if showBackItem:
        allMenuItemNames.append("Back")
        backIndex = len(allMenuItemNames) - 1
    print("{0}:".format(menuName))
    for menuItem in allMenuItemNames:
        menuNum += 1
        print("-({0}) {1}".format(menuNum, menuItem))

    userSelection = getUserInput(menuNum) - 1
    if userSelection == backIndex:
        return -1
    return userSelection



def getUserInput(menuNum):
    while True:
        userSelection = input(":  ")
        try:
            userSelection = int(userSelection)
        except ValueError:
            print("Not a valid selection.")
            continue
        if userSelection not in range(1, menuNum + 1):
            print("Selection must be between 1 and {0}".format(menuNum))
            continue
        return userSelection


main()