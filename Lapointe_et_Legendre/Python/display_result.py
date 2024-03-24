import numpy as np


def load_data():
	# Read all files and prepare the data first
	## Prepare distillery names
	with open('../Data/Transformation/distillery.csv') as f:
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

# Return recommendation based on user's selection
## If there user's selection, use 84 (McCallan)
def get_recommendation(results, num2dis, fav_whisky=84):
	# Select a whisky first
	selected = enumerate(results[fav_whisky].tolist())

	# Display Result
	recommendation = sorted(selected, key=lambda x: x[1])[1:6]
	recommendation = [(num2dis[i], i, score) for i, score in recommendation]
	print(recommendation)

def interact(results, dis2num, num2dis):
	repeat = True
	while repeat:
		menu_selection = homepage()
		if menu_selection == 1:
			print('Coming soon!')
		elif menu_selection == 2:
			print('You may try McCallan! And also:')
			get_recommendation(results, num2dis)
		repeat = repeat_or_not()

def main():
	results, dis2num, num2dis = load_data()
	interact(results, dis2num, num2dis)

main()
