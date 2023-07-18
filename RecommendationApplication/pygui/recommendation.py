import pandas as pd


"""
def similar_recommendation():
	firstwhisky_index, firstwhisky = sc.getWhisky(whiskynames)
    cluster = whisky2group[firstwhisky]
    
    """
    """
    # Use this block if sort by physical distilleries distance
    firstwhisky_loc = [whiskydata.loc[whiskydata.index[firstwhisky_index],'Lat'],
                       whiskydata.loc[whiskydata.index[firstwhisky_index],'Lon']]
    recommendation = whiskydata[whiskydata['Cluster']==cluster]
    recommendation['distance'] = np.linalg.norm(recommendation[['Lat','Lon']]
                                    .sub(np.array(firstwhisky_loc)), axis=1)
    """
    """
    # Use this blick if sort by flavor similarity
    whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                       'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                       'Floral']
    firstwhisky_loc = whiskydata.loc[whiskydata.index[firstwhisky_index],
                                     whisky_features]
    firstwhisky_loc = firstwhisky_loc.values
    recommendation = whiskydata[whiskydata['Cluster']==cluster]
    recommendation['distance'] = recommendation[whisky_features] \
                                   .sub(np.array(firstwhisky_loc)).pow(2) \
                                   .sum(1).pow(0.5)
    recommendation = recommendation.sort_values(by=['distance'])
    # Remove the first element which is a duplicated entry
    recommendation = recommendation['Distillery'].tolist()[1:]
"""

def flavour_recommendation(whisky_pdframe, choice_flavour, num_choice_strength, whisky_features, strengthlist):
	# Check if the strength of the flavor exist in the data set
	
	i_whisky_pdframe = whisky_features.index(choice_flavour)
	uniquevalues = whisky_pdframe.iloc[:,i_whisky_pdframe].unique().tolist()
	if num_choice_strength not in uniquevalues:
		# Delete Later
		print('No such whisky, but we would tune down the strength')
		# Find the next value below the original strength score
		while num_choice_strength not in uniquevalues:
			num_choice_strength -= 1
		# Delete Later
		print(f'We will find {strengthlist[num_choice_strength]} {choice_flavour}',
			  'for you.')
	recommendation = whisky_pdframe[whisky_pdframe.iloc[:,i_whisky_pdframe]==num_choice_strength]
	recommendation = recommendation['Distillery'].tolist()
	# Delete later
	print(recommendation)