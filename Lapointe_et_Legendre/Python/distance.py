import pandas as pd
import numpy as np


# Read Data of Whisky characteristics
df = pd.read_csv('../Data/Transformation/whisky_characters.csv')

# np.zero for final distance deliverable
num_distilleries = len(df)
distance = np.zeros(shape=(num_distilleries, num_distilleries))

# Do the calculation
for i in range(num_distilleries):
	for j in range(1, num_distilleries):
		if i != j:
			row_i = df.drop(['name'],axis=1).iloc[i].to_numpy()
			row_j = df.drop(['name'],axis=1).iloc[j].to_numpy()
			curr_dis = np.linalg.norm(row_i-row_j)
			distance[i][j] = curr_dis
			distance[j][i] = curr_dis

np.savetxt('distance.txt', distance, delimiter='\t', fmt='%f')
