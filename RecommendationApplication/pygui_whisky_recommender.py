import pandas as pd
import tkinter as tk
from pygui.gui_helper import *
from pydata.load_data import *


# Window Configuration
gui = tk.Tk()
gui.geometry('500x300')
gui.title('Whisky Recommender')

whiskydata, whiskynames, whisky2group = get_data('../Clusters/Results/whisky_with_cluster.csv')
display_frontpage(whiskydata, whiskynames, whisky2group)

gui.mainloop()