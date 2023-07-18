import pandas as pd


def getWhiskyName(whiskynames: list):
    numWhisky = len(whiskynames)

    menuDistilleries = ""
    for i in range(numWhisky):
        menuDistilleries += str(i+1)
        menuDistilleries += " - "
        menuDistilleries += whiskynames[i]
        if i != numWhisky - 1:
            menuDistilleries += "\n"

    choice = -1
    counter = 0
    while choice < 1 or choice > numWhisky:
        if counter > 0:
            print("Please try again.")
        print("Please choose the folloing distillery by entering between 1 and",
              numWhisky)
        print(menuDistilleries)
        choice = int(input("Enter your choice:"))
        counter += 1

    return whiskynames[choice-1]


def getWhisky(whiskynames: list):
    firstwhisky = input("Enter your favourite whisky: ")
    print("You have entered:", firstwhisky)
    counter = 0
    validname = False
    firstwhisky_index = -1
    if firstwhisky in whiskynames:
        validname = True

    while counter < 2 and validname is False:
        print("The whisky distillery name you have entered is not on the list.")
        print("Please try again")
        firstwhisky = input("Enter your favourite whisky: ")
        print("You have entered:", firstwhisky)
        counter += 1
        if firstwhisky in whiskynames:
            validname = True

    if validname is False:
        firstwhisky = sc.getWhiskyName(whiskynames)
        print("You have entered:", firstwhisky)

    firstwhisky_index = whiskynames.index(firstwhisky)

    return firstwhisky_index, firstwhisky


def getWhiskyByFlavor(whisky_pdframe):
    # Menu script
    menuFlavor = "Please select the following option:\n"
    menuFlavor += "1 - Body\n"
    menuFlavor += "2 - Sweetness\n"
    menuFlavor += "3 - Smoky\n"
    menuFlavor += "4 - Medicinal\n"
    menuFlavor += "5 - Tobacco\n"
    menuFlavor += "6 - Honey\n"
    menuFlavor += "7 - Spicy\n"
    menuFlavor += "8 - Winey\n"
    menuFlavor += "9 - Nutty\n"
    menuFlavor += "10 - Malty\n"
    menuFlavor += "11 - Fruity\n"
    menuFlavor += "12 - Floral\n"
    menuFlavor += "\n"
    menuFlavor += "If you cannot decide, select '0'"

    # List of flavor and strength
    choicelist = ['Cannot decide', 'Body', 'Sweetness', 'Smoky', 'Medicinal',
                  'Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty',
                  'Fruity', 'Floral']
    strengthlist = ['None', 'Light', 'Medium', 'Strong', 'Very strong']

    # Obtain flavor
    choice = -1
    print(menuFlavor)
    choice = int(input("Enter your choice:"))

    while choice < 0 and choice > 12:
        print("Invalid answer, please try again")
        print(menuFlavor)
        choice = int(input("Enter your choice:"))

    print('You have choosen:', choicelist[choice])

    # If user cannot decide, return None
    if choice == 0:
        return None

    # Obtain Strength of flavor
    menustrength = "Please the strength from 1 - 4, ranging from"
    for strength in strengthlist:
        menustrength += " "
        menustrength += strength
    menustrength += "."
    print(menustrength)
    strength_choice = int(input("Enter your choice:"))
    while strength_choice < 1 and strength_choice > 4:
        print("Invalid answer, please try again")
        print(menustrength)
        choice = int(input("Enter your choice:"))
    print('You have choosen:', choicelist[choice])

    print('You choice is:', strengthlist[strength_choice], choicelist[choice])

    # Check if the strength of the flavor exist in the data set
    uniquevalues = whisky_pdframe.iloc[:, choice].unique().tolist()
    if strength_choice not in uniquevalues:
        print('No such whisky, but we would tune down the strength')
        # Find the next value below the original strength score
        while strength_choice not in uniquevalues:
            strength_choice -= 1
        print('We will find', strengthlist[strength_choice], choicelist[choice],
              'for you.')

    # Filter the list accordingly
    recommendation = whisky_pdframe[whisky_pdframe.iloc[:,
                                                        choice] == strength_choice]
    recommendation = recommendation['Distillery'].tolist()

    return recommendation


menu = "Please select the following option:\n"
menu += "1 - Start by entering whisky name\n"
menu += "2 - Start by choosing flavor\n"
menu += "3 - No idea where to start"
