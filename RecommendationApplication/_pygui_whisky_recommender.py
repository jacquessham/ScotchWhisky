import tkinter as tk
from pygui

# GUI helper function
def frontpage_selection(event):
	selection = frontpage_dropdown.get()
	choice = int(selection[0])

	if choice == 1:
		fame_second_choice = tk.Frame()
		headline_secondchoice = tk.Label(master=fame_second_choice, text='Choice from different dropdown')
		headline_secondchoice.pack()
		fame_second_choice.pack()

	else:
		messagebox.showinfo(
			title='Selection',
			message=f"You may try MaCallan"
			)


# Window Configuration
gui = tk.Tk()
gui.geometry('500x300')
gui.title('Whisky Recommender')

# Frame
frame_main = tk.Frame()
frame_frontpage_question = tk.Frame()
frame_frontpage_dropdown = tk.Frame()


headline = tk.Label(master=frame_main, text='Welcome to the Whisky Recommender')
headline.pack()

frontpage_question = tk.Label(master=frame_frontpage_question,
	text='Please select the following option:')
frontpage_question.pack()

frontpage_dropdown_menu = ['1 - Start by entering whisky name', '2 - Start by choosing flavor','3 - No idea where to start']
frontpage_dropdown = ttk.Combobox(
	state='readonly',
	values=frontpage_dropdown_menu,
	width=30
	)
frontpage_dropdown.bind("<<ComboboxSelected>>", frontpage_selection)
frame_main.pack()
frame_frontpage_question.pack()
frontpage_dropdown.pack()


gui.mainloop()