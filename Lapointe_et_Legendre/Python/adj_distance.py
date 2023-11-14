import json
import pandas as pd
import numpy as np


# Convert column index to type
def col_i2type(i):
	if i < 14: return 'color'
	elif i < 26: return 'nose'
	elif i < 34: return 'body'
	elif i < 42: return 'palate'
	else: 
		return 'finish'

# Calculate the distance
def calculate_distance(row_i, row_j, i2col_type, char_num, char_types):
	# Calculate the coeff first
	coeff = {}

	# Scan through row_i and row_j to find mutual characters
	# Mutual characters mean any character appear in either at least once
	for char_type in char_types:
		mutual_char = 0
		for i in range(len(row_i)):
			if row_i[i] == 1 and i2col_type[i][1] == char_type:
				mutual_char += 1
			elif row_j[i] == 1 and i2col_type[i][1] == char_type:
				mutual_char += 1
		# Calculate the coeff and store other calculation
		coeff[char_type] = {
			'mutual_char': mutual_char,
			'coeff': mutual_char/char_num[char_type],
			# Use for dominator calculation
			'coeff_sum': mutual_char * (mutual_char/char_num[char_type])

			}
	# Assign coeff to every entry
	arr_coeff = [coeff[i2col_type[i][1]]['coeff'] for i in range(len(row_i))]

	# Calculate eudlidean distance times coeff
	nomin = sum((row_i-row_j)**2*arr_coeff)

	# Sum the coeff used (If row_i and row_j both 0, coeff will not be used)
	domin = 0
	for char_type in char_types:
		domin += coeff[char_type]['coeff_sum']

	# Return the calculation
	return nomin/domin


# Read Data of Whisky characteristics
df = pd.read_csv('../Data/Transformation/whisky_characters.csv')

# Obtain the file names and their column names within the file
with open('../Data/Transformation/columns.json','r') as f_cols:
	type2col = json.load(f_cols)

# Convert type2col to col2type
char_types = [char_type for char_type in type2col if char_type != 'distillery'] 

# Hard code this because column names are not consistent
char_num = {
	'color': 14,
	'nose': 12,
	'body': 8,
	'palate': 15,
	'finish': 19
}

df_cols = df.drop(['name'],axis=1).columns.tolist()

# Prepare dictionaries for easy convertion
col2type = {}
for char_type in char_types:
	for col in type2col[char_type]:
		col2type[col] = (char_type, df_cols.index(col))

i2col_type = {}
for i in range(len(df_cols)):
	i2col_type[i] = (df_cols[i], col_i2type(i))

# np.zero for final distance deliverable
num_distilleries = len(df)
distance = np.zeros(shape=(num_distilleries, num_distilleries))

# Do the calculation
for i in range(num_distilleries):
	for j in range(1, num_distilleries):
		if i != j:
			row_i = df.drop(['name'],axis=1).iloc[i].to_numpy()
			row_j = df.drop(['name'],axis=1).iloc[j].to_numpy()
			curr_dis = calculate_distance(row_i, row_j, i2col_type, 
				char_num ,char_types)
			distance[i][j] = curr_dis
			distance[j][i] = curr_dis

print(distance)

np.savetxt('adj_distance.txt', distance, delimiter='\t', fmt='%f')