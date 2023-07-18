import pandas as pd
import tkinter as tk
from pygui.gui_helper import *


# Window Configuration
gui = tk.Tk()
gui.geometry('500x300')
gui.title('Whisky Recommender')

whisky = pd.read_csv('../Data/whisky.csv')
display_frontpage()

gui.mainloop()