import numpy as np
import pandas as pd
import statistics as stats
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def k_folds_logreg(k, dataset, features, col_categories, rs):
    rows_num = dataset.shape[0] # Get nrow
    rows_fold = int(rows_num/k) # Get numbers of row for every fold
    rows_array = np.arange(num_row) # Get an array of 0 to last index
    np.random.seed(rs)
    np.random.shuffle(rows_array) # shuffle the indexes
    
    # Convert label in string to int
    dataset_regions = dataset[col_categories].unique().tolist()
    cat2labels = {}
    labels2cat = {}
    for i in range(len(dataset_regions)):
        cat2labels[dataset_regions[i]] = i
        labels2cat[i] = dataset_regions[i]
    dataset['label_int'] =  dataset[col_categories].map(cat2labels)
    
    # Get an empty list to store results
    clf_acc_list = []
    svc_acc_list = []
    dt_acc_list = []
    rf_acc_list = []
    
    
    for i in range(k):
        if (i != 0 and i != k-1):
            val_rows = rows_array[i*rows_fold:(i+1)*rows_fold]
        elif i == 0:
            val_rows = rows_array[:rows_fold]
        else:
            val_rows = rows_array[i*rows_fold:]
        train_rows = [row for row in rows_array if row not in val_rows]
        
        # Prepare data
        train_X = dataset.loc[rows_array[train_rows],features]
        train_y = dataset.loc[rows_array[train_rows],'label_int']
        val_X = dataset.loc[rows_array[val_rows],features]
        val_y = dataset.loc[rows_array[val_rows],'label_int']
        
        # Fit models
        clf = LogisticRegression(random_state=rs).fit(train_X, train_y)
        clf_acc = clf.score(val_X, val_y)
        svc = SVC(kernel='linear', random_state=rs).fit(train_X, train_y)
        svc_acc = svc.score(val_X, val_y)
        dt = DecisionTreeClassifier(random_state=rs).fit(train_X, train_y)
        dt_acc = dt.score(val_X, val_y)
        rf = RandomForestClassifier(random_state=rs).fit(train_X, train_y)
        rf_acc = rf.score(val_X, val_y)
        clf_acc_list.append(clf_acc)
        svc_acc_list.append(svc_acc)
        dt_acc_list.append(dt_acc)
        rf_acc_list.append(rf_acc)

    return {'clf':clf_acc_list, 'svc':svc_acc_list, 'dt':dt_acc_list,'rf':rf_acc_list}

whisky = pd.read_csv('whisky.csv')
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
results = k_folds_logreg(5, whisky, whisky_features, 'Region', 49)
print(results)
