import numpy as np
import pandas as pd
import script as sc


# Subpress warings
pd.set_option('mode.chained_assignment', None)
# Read file
whiskydata = pd.read_csv("../whisky_with_cluster.csv")
# Obtain the list of distilleries for function parameters
whiskynames = whiskydata['Distillery'].tolist()
# Build name to cluster and cluster to name dictionaries
whisky2group = dict(zip(whiskydata.Distillery.values, 
                        whiskydata.Cluster.values))
groups_list = whiskydata['Cluster'].unique().tolist()
group2whisky = {}
for group in groups_list:
    group2whisky[group] = []
for name, cluster in zip(whiskydata.Distillery.values, 
                         whiskydata.Cluster.values):
    group2whisky[cluster].append(name)

# UI
print(sc.menu)
recommend_method = int(input("Enter your choice: "))
while (recommend_method < 1 or recommend_method > 3):
    print("Your input is invalid, please choose enter the valid option.")
    print(sc.menu)
    recommend_method  = int(input("Enter your choice:"))

if recommend_method == 1:
    firstwhisky_index, firstwhisky = sc.getWhisky(whiskynames)
    cluster = whisky2group[firstwhisky]

    firstwhisky_loc = [whiskydata.loc[whiskydata.index[firstwhisky_index],'Lat'],
                       whiskydata.loc[whiskydata.index[firstwhisky_index],'Lon']]
    recommendation = whiskydata[whiskydata['Cluster']==cluster]
    recommendation['distance'] = np.linalg.norm(recommendation[['Lat','Lon']]
                                    .sub(np.array(firstwhisky_loc)), axis=1)
    recommendation = recommendation.sort_values(by=['distance'])
    # Remove the first element which is a duplicated entry
    recommendation = recommendation['Distillery'].tolist()[1:]
elif recommend_method == 2:
    recommendation = sc.getWhiskyByFlavor(whiskydata)
elif recommend_method == 3:
    recommendation = None

# Display result
if recommendation is not None:
    if recommend_method == 1:
        print("This is the list of recommendation in order:")
    elif recommend_method == 2:
        print("This is the list of recommendation in alphabetical order:")
    counter = 1
    for distillery in recommendation:
        print(counter,'. ',distillery, sep='')
        counter += 1
else:
    print("Choose Macallan.")

