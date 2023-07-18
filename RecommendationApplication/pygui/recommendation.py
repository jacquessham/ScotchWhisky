import pandas as pd
import numpy as np


def check_whiskyname(name, whiskynames):
    if name in whiskynames:
        return True
    return False


def similar_recommendation(whiskydata, user_input, whiskynames,
                           whisky2group, whisky_features):
    firstwhisky = user_input.lower().strip()

    # Validiate user input
    if not check_whiskyname(firstwhisky, whiskynames):
        return False, []

    cluster = whisky2group[firstwhisky]
    i_firstwhisky = whiskynames.index(firstwhisky)

    # Sort by flavor similarity
    firstwhisky_loc = whiskydata.loc[whiskydata.index[i_firstwhisky],
                                     whisky_features]
    firstwhisky_loc = firstwhisky_loc.values
    recommendation = whiskydata[whiskydata['Cluster'] == cluster]
    recommendation['distance'] = recommendation[whisky_features] \
        .sub(np.array(firstwhisky_loc)).pow(2) \
        .sum(1).pow(0.5)
    recommendation = recommendation.sort_values(by=['distance'])
    # Remove the first element which is a duplicated entry
    recommendation = recommendation['Distillery'].tolist()[1:]

    return True, recommendation


def flavour_recommendation(whisky_pdframe, choice_flavour,
                           num_choice_strength, whisky_features,
                           strengthlist):
    # Check if the strength of the flavor exist in the data set

    i_whisky_pdframe = whisky_features.index(choice_flavour)
    uniquevalues = whisky_pdframe.iloc[:, i_whisky_pdframe].unique().tolist()
    if num_choice_strength not in uniquevalues:
        # Find the next value below the original strength score
        while num_choice_strength not in uniquevalues and \
                num_choice_strength > 0:
            # Tune down the strength.
            # Assumption: Users more likely accept weaker flavour
            num_choice_strength -= 1

    recommendation = whisky_pdframe[whisky_pdframe.iloc[:, i_whisky_pdframe] ==
                                    num_choice_strength]
    return recommendation['Distillery'].tolist()
