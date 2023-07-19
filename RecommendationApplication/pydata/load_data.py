import pandas as pd


def get_data(filename):
    pd.set_option('mode.chained_assignment', None)
    # Read file
    whiskydata = pd.read_csv(filename)
    # Obtain the list of distilleries for function parameters for Choice 1
    whiskynames = [distillery.lower()
                   for distillery in whiskydata['Distillery'].tolist()]
    # Build name to cluster and cluster to name dictionaries
    whisky2group = dict(zip(whiskynames, whiskydata.Cluster.values))
    groups_list = whiskydata['Cluster'].unique().tolist()

    return whiskydata, whiskynames, whisky2group
