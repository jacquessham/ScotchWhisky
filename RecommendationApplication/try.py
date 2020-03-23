import numpy as np
import pandas as pd

whiskydata = pd.read_csv("../whisky_with_cluster.csv")
"""
first_lat = whiskydata.loc[whiskydata.index[0],'Lat']
first_lon = whiskydata.loc[whiskydata.index[0],'Lon']

print(first_lat)
print(first_lon)

location = [first_lat, first_lon]
print(location)

whiskydata['distance'] = np.linalg.norm(whiskydata[['Lat','Lon']].sub(np.array(location)), axis=1)

print(whiskydata[['Lat','Lon','distance']])
"""

print(whiskydata[whiskydata['Cluster']==3])