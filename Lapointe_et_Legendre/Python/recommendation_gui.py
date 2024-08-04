import pandas as pd
import tkinter as tk
from gui_helper import *
from recommendation_flow import *


# Window Configuration
gui = tk.Tk()
gui.geometry('800x1000')
gui.title('Whisky Recommender')

# Load Data
results, dis2num, num2dis = main(True)
display_frontpage(results, num2dis)

gui.mainloop()