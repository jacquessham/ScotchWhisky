import numpy as np


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

# Select a whisky first
fav_whisky = 19
selected = enumerate(results[fav_whisky].tolist())

# Display Result
recommendation = sorted(selected, key=lambda x: x[1])[1:6]
recommendation = [(num2dis[i], i, score) for i, score in recommendation]
print(recommendation)
