import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


# Function to train model and produce results
def classify_whisky(n_class, X, label, rs):
    # Fit model and predict results
    cluster_machine = KMeans(n_clusters=n_class, random_state=rs).fit(X)
    pred = cluster_machine.predict(X)
    # Declare a dictionary and empty lists for each group
    whisky_groups = {}
    for i in range(n_class):
        whisky_groups[i] = []
    # Append the distillery names into the their assigned group
    for distillery, group in zip(labels['Distillery'].tolist(), pred):
        whisky_groups[group].append(distillery)
    return whisky_groups, pred

# Read File
whisky = pd.read_csv('../Data/whisky.csv')
# The below lines are for additional data
"""
filepath = None
whisky_more = pd.read_csv(filepath)
whisky = pd.concat([whisky, whisky_more])
"""
# Select the features needed
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
# Get the features and distillery names from the data set
X = whisky[whisky_features]
labels = whisky[['Distillery']]

whisky_recommendation, pred = classify_whisky(6, X, labels, 0)


# Save the results to text files for displaying purpose
filename = 'Results/whisky_recommendation.txt'
result_file = open(filename, 'w')
for i in whisky_recommendation:
    result_file.write('Group ')
    result_file.write(str(i+1))
    result_file.write(': ')
    for j in range(len(whisky_recommendation[i])):
        if j != len(whisky_recommendation[i])-1:
            result_file.write(whisky_recommendation[i][j])
            result_file.write(', ')
        else:
            result_file.write(whisky_recommendation[i][j])
    result_file.write('\n')
    result_file.write('\n')
result_file.close()

# Add a column to whisky.csv for grouping
pred += 1 # Increment 1 to turn 0-base to 1-base cluster
pred = pd.DataFrame(pred, columns=['Cluster'])
whisky = pd.concat([whisky,pred], axis=1)
whisky.to_csv('Results/whisky_with_cluster.csv', index=False)