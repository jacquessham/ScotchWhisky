import numpy as np
import pandas as pd
import statistics as stats
from sklearn.linear_model import LogisticRegression

whisky = pd.read_csv('whisky.csv')
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
train_X = whisky[whisky_features]

whisky_regions = whisky['Region'].unique().tolist()
cat2labels = {}
labels2cat = {}
for i in range(len(whisky_regions)):
    cat2labels[whisky_regions[i]] = i
    labels2cat[i] = whisky_regions[i]
whisky['label_int'] =  whisky['Region'].map(cat2labels)
train_y = whisky['label_int']

rs = 49

clf = LogisticRegression(random_state=rs).fit(train_X, train_y)
print(clf.score(train_X, train_y))
clf_pred_result = clf.predict(train_X)

whisky_regions_pred = []
for i in clf_pred_result:
	whisky_regions_pred.append(labels2cat[i])

results = {'Distillery': whisky['Distillery'],
           'Lat': whisky['Lat'],
           'Lon': whisky['Lon'],
           'Region_Correct': whisky['Region'],
           'Region_Prediction': whisky_regions_pred}

results = pd.DataFrame(results)
results.to_csv('whisky_clf_pred.csv', index=False)
results_wrong = results[results['Region_Correct']!= \
                        results['Region_Prediction']]
results_wrong.to_csv('whisky_clf_wrongpred.csv', index=False)