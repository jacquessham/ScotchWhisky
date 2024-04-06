from sys import argv
import numpy as np


def load_data(data='adjusted'):
	# Read all files and prepare the data first
	## To load distance trained with Lapointe and Legendre Algo
	if data == 'adjusted':
		filename = 'adj_distance.txt'
	## To load original distance (Standard Similarity)
	elif data == 'standard':
		filename = 'distance.txt'
	else:
		print('Input invalid...using adj_distance.txt')
		filename = 'adj_distance.txt'

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
	results = np.loadtxt(filename, dtype=float)

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
		# Ensure user's input is valid
		try:
			fav_whisky = int(fav_whisky)-1
			# Ensure user selected within the range
			if fav_whisky > len(num2dis) or fav_whisky < 0:
				print('You selection is invalid, please try again!')
				fav_whisky = None
		# Repeat the loop if invalid
		except:
			print('You selection is invalid, please try again!')
			fav_whisky = None
	return fav_whisky


# Display recommendations in a beautified format
def display_recommendation(fav_whisky, recommendations, dev_mode=False):
	print(f'Here is the recommendations that is similar to {fav_whisky}:')
	if dev_mode:
		print(f'Order\tDistilleries\t\tDistance')
	else:
		print(f'Order\tDistilleries')
	for i, recommend in enumerate(recommendations):
		if dev_mode:
			print(f'{i+1}\t{recommend[0]:20}\t{recommend[2]}')
		else:
			print(f'{i+1}\t{recommend[0]:20}')


# Return recommendation based on user's selection
## If there user's selection, use 84 (McCallan)
def get_recommendation(results, num2dis, fav_whisky_num=84, dev_mode=False):
	# Select a whisky first
	selected = enumerate(results[fav_whisky_num].tolist())

	# If dev_mode, ask how many whiskies to recommend
	if dev_mode:
		valid = False
		while not valid:
			num_input = input('How many whiskies do you wish to recommend? ')
			try:
				top = int(num_input)
				if top > 0: 
					valid = True
				else:
					print('Please enter a number greater than 1!')
			except:
				print('Invalid input...please try again!')
	# If not dev_mode, just show top 5
	else:
		top = 5
	# Display Result
	recommendations = sorted(selected, key=lambda x: x[1])[1:top+1]
	# recommendation is (distillery_name, distillery_index, similarity_score)
	recommendations = [(num2dis[i], i, score) for i, score in recommendations]
	display_recommendation(num2dis[fav_whisky_num], recommendations, dev_mode)

def interact(results, dis2num, num2dis, dev_mode=False):
	repeat = True
	while repeat:
		menu_selection = homepage()
		# Have user to pick a whisky
		if menu_selection == 1:
			fav_whisky = pick_distillery(num2dis)
			print(f'The favourite whisky is {num2dis[fav_whisky]}')
			get_recommendation(results, num2dis, fav_whisky, dev_mode)
		# User has no where to get started
		elif menu_selection == 2:
			print('You may try McCallan! And also:')
			get_recommendation(results, num2dis, dev_mode=dev_mode)
		# Ask user if he wants to repeat the inquire again
		repeat = repeat_or_not()

def is_dev_mode(argv):
	if argv[1].lower() == 'dev':
		print('Entering developer mode...')
		return True
	print('Invalid input, entering in production mode...')
	return False

def main():
	# Load adj_distance.txt or distance.txt
	data = 'adjusted'
	# When user did not enter any argument
	if len(argv)-1 == 0:
		dev_mode = False
	# When user only enter dev mode
	elif len(argv)-1 == 1:
		dev_mode = is_dev_mode(argv)
	# When user enter dev mode and use standard data
	elif len(argv)-1 == 2:
		dev_mode = is_dev_mode(argv)
		if dev_mode and argv[2] == 'standard':
			print('Using Standard Similarity Data')
			data = 'standard'
		# When dev_mode is true but argv[2] input is invalid
		elif dev_mode:
			print(f'{argv[2]} is an invalid input, using adj_distance.txt')
	else:
		print('Invalid input, entering in production mode...')
		dev_mode = False

	results, dis2num, num2dis = load_data(data)
	interact(results, dis2num, num2dis, dev_mode)

main()
