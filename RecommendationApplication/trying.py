#Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Initialize a Frame
frame = Frame(win)

def clear_all():
   for item in frame.winfo_children():
      item.destroy()
      button.config(state= "disabled")

#Define a ListBox widget
listbox = Listbox(frame, height=10, width= 15, bg= 'grey', activestyle= 'dotbox',font='aerial')
listbox.insert(1,"Go")
listbox.insert(1,"Java")
listbox.insert(1,"Python")
listbox.insert(1,"C++")
listbox.insert(1,"Ruby")

listbox.pack()

label = Label(win, text= "Top 5 Programming Languages", font= ('Helvetica 15 bold'))
label.pack(pady= 20)
frame.pack()

#Create a button to remove all the children in the frame
button = Button(win, text= "Clear All", font= ('Helvetica 11'), command= clear_all)
button.pack()

win.mainloop()