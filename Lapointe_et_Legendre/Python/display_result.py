import numpy as np


def load_data():
	# Read all files and prepare the data first
	## Prepare distillery names
	with open('../Data/Transformation/distillery.csv') as f:
		# Remove header, first entry will have index=0
		distilleries = f.read().splitlines()[1:]
	dis2num = {}
	num2dis = {}
	for num, dis in enumerate(distilleries):
		dis2num[dis] = num
		num2dis[num] = dis

	## Read the result
	results = np.loadtxt('adj_distance.txt',dtype=float)

	return results, dis2num, num2dis

def homepage():
	menu_selection = None
	while menu_selection not in [1,2]:
		print('Please select from the following options by input the selection number:')
		print('1. Pick a distillery')
		print('2. No idea where to start')
		menu_selection = input('Your selection: ').strip()
		try:
			menu_selection = int(menu_selection)
		except:
			print('You selection is invalid, please try again!')
			menu_selection = None
	return menu_selection

def repeat_or_not():
	menu_selection = None
	while menu_selection not in [1,2]:
		print('Do you want another recommendation?')
		print('1. Yes')
		print('2. No')
		menu_selection = input('Your selection: ').strip()
		try:
			menu_selection = int(menu_selection)
		except:
			print('You selection is invalid, please try again!')
			menu_selection = None
	if menu_selection == 1:
		return True
	return False

# Obtain user's input on his fav_whisky
def pick_distillery(num2dis):
	fav_whisky = None
	while fav_whisky not in num2dis.keys():
		print('Please select a distillery below:')
		for k in num2dis.keys():
			print(f'{k+1}: \t{num2dis[k]}')
		fav_whisky = input('Your selection: ').strip()
		try:
			fav_whisky = int(fav_whisky)-1
		except:
			print('You selection is invalid, please try again!')
			fav_whisky = None
	return fav_whisky


# Display recommendations in a beautified format
def display_recommendation(fav_whisky, recommendations):
	print(f'Here is the recommendations that is similar to {fav_whisky}:')
	print(f'Order\tDistilleries')
	for i, recommend in enumerate(recommendations):
		print(f'{i+1}\t{recommend[0]}')


# Return recommendation based on user's selection
## If there user's selection, use 84 (McCallan)
def get_recommendation(results, num2dis, fav_whisky_num=84):
	# Select a whisky first
	selected = enumerate(results[fav_whisky_num].tolist())

	# Display Result
	recommendations = sorted(selected, key=lambda x: x[1])[1:6]
	recommendations = [(num2dis[i], i, score) for i, score in recommendations]
	# print(recommendations)
	display_recommendation(num2dis[fav_whisky_num], recommendations)

def interact(results, dis2num, num2dis):
	repeat = True
	while repeat:
		menu_selection = homepage()
		# Have user to pick a whisky
		if menu_selection == 1:
			fav_whisky = pick_distillery(num2dis)
			print(f'The favourite whisky is {fav_whisky}')
			get_recommendation(results, num2dis, fav_whisky)
		# User has no where to get started
		elif menu_selection == 2:
			print('You may try McCallan! And also:')
			get_recommendation(results, num2dis)
		# Ask user if he wants to repeat the inquire again
		repeat = repeat_or_not()

def main():
	results, dis2num, num2dis = load_data()
	interact(results, dis2num, num2dis)

main()
