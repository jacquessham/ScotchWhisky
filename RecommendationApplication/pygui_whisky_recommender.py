import pandas as pd
import tkinter as tk
from pygui.gui_helper import *
from pydata.load_data import *


# Window Configuration
gui = tk.Tk()
gui.geometry('800x1000')
gui.title('Whisky Recommender')

# Load Data
filename = '../Clusters/Results/whisky_with_cluster.csv'
whiskydata, whiskynames, whisky2group = get_data(filename)

# Render GUI Layout
display_frontpage(whiskydata, whiskynames, whisky2group)

gui.mainloop()