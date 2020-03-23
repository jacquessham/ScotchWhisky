def getWhiskyName(whiskynames:list):
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
		print("Please choose the folloing distillery by entering between 1 and", \
		  numWhisky)
		print(menuDistilleries)
		choice = int(input("Enter your choice:"))
		counter += 1

	return whiskynames[choice-1]

def getWhisky(whiskynames:list):
	firstwhisky = input("Enter your favourite whisky: ")
	print("You have entered:",firstwhisky)
	counter = 0
	validname = False
	firstwhisky_index = -1
	if firstwhisky in whiskynames:
		validname = True

	while counter < 2 and validname is False:
		print("The whisky distillery name you have entered is not on the list.")
		print("Please try again")
		firstwhisky = input("Enter your favourite whisky: ")
		print("You have entered:",firstwhisky)
		counter += 1
		if firstwhisky in whiskynames:
			validname = True

	if validname is False:
		firstwhisky = sc.getWhiskyName(whiskynames)
		print("You have entered:",firstwhisky)

	firstwhisky_index = whiskynames.index(firstwhisky)

	return firstwhisky_index, firstwhisky

menu = "Please select the following option:\n"
menu += "1 - Start by entering whisky name\n"
menu += "2 - Start by choosing flavor\n"
menu += "3 - No idea where to start"