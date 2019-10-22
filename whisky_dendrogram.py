import pandas as pd
import plotly
import plotly.figure_factory as ff
from plotly.offline import *
# To initiate ploty to run offline
init_notebook_mode(connected=True)

whisky = pd.read_csv('whisky.csv')
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral']
whisky_data = whisky[whisky_features]
distilleries = whisky['Distillery'].tolist()

choice_viz = ff.create_dendrogram(whisky_data, orientation='bottom',
	                              labels=distilleries)
choice_viz['layout'].update({'width':1400, 'height':600,
	                         'title': 'Recommendation of Scotch Whisky',
	                         'yaxis': {'title':'Distance'}})
plotly.offline.plot(choice_viz, filename='whisky_dendrogram.html')