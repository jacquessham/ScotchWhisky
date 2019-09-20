import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def classify_whisky(n_class, X, label, rs):
    cluster_machine = KMeans(n_clusters=n_class, random_state=rs).fit(X)
    pred = cluster_machine.predict(X)
    whisky_groups = {}
    for i in range(n_class):
        whisky_groups[i] = []
    for distillery, group in zip(labels['Distillery'].tolist(), pred):
        whisky_groups[group].append(distillery)
    return whisky_groups

whisky = pd.read_csv('whisky.csv')

whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
X = whisky[whisky_features]
labels = whisky[['Distillery']]

whisky_recommendation = classify_whisky(8, X, labels, 0)