import os
import json
import pandas as pd


# Read unix file
def read_unix(filename: str, colnames: list):
	data = []
	with open(filename, 'r') as curr_f:
		for i, line in enumerate(curr_f):
			# First line is file summary
			if i != 0:
				curr_line = line.replace('  ',' ').strip().split(' ')
				if len(curr_line) == len(colnames):
					data.append(curr_line)
	return pd.DataFrame(data, columns=colnames)

# Obtain the file names and their column names within the file
with open('columns.json','r') as f_cols:
	file2col = json.load(f_cols)

# Dict to store all data
data = {}

# List of Distillery are in the current directory
data['distillery'] = pd.read_csv('distillery.csv')

# Change directory to read character files
directory_origin = os.getcwd()
os.chdir('../OriginalData/Scotch data (Unix)')

# Read character files
for f in os.listdir(os.getcwd()):
	curr_f = f.split('(')[0] # E.g. Convert filename from color(109x14) -> color
	# There are some irrelevant 
	if curr_f in file2col:
		# Save file data into data dictionary
		data[curr_f] = read_unix(f, file2col[curr_f])

# Merge all data
df = pd.concat([data[k] for k in data.keys()], axis=1)

# Save Data in the original directory
os.chdir(directory_origin)
df.to_csv('whisky_characters.csv',index=False)

