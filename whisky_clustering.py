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
    return whisky_groups

# Read File
whisky = pd.read_csv('../whisky.csv')
# Select the features needed
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
# Get the features and distillery names from the data set
X = whisky[whisky_features]
labels = whisky[['Distillery']]

# Try 3-12 classes
for i in range(3,13):
    whisky_recommendation = classify_whisky(i, X, labels, 0)
    # Save the results to text files
    filename = 'Results/whisky_cluster_results_'
    filename += str(i) + '.txt'
    result_file = open(filename, 'w')
    for j in whisky_recommendation:
        result_file.write('Group ')
        result_file.write(str(j+1))
        result_file.write(': ')
        for k in range(len(whisky_recommendation[j])):
            if k != len(whisky_recommendation[j])-1:
                result_file.write(whisky_recommendation[j][k])
                result_file.write(', ')
            else:
                result_file.write(whisky_recommendation[j][k])
        result_file.write('\n')
        result_file.write('\n')
    result_file.close()


