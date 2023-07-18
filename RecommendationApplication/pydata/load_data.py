import pandas as pd


def get_data(filename):
	pd.set_option('mode.chained_assignment', None)
	# Read file
	whiskydata = pd.read_csv(filename)
	# Obtain the list of distilleries for function parameters
	whiskynames = whiskydata['Distillery'].tolist() # For Choice 1
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

	return whiskydata, whiskynames, whisky2group