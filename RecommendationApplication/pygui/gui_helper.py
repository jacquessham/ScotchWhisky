from tkinter import messagebox, ttk, RIDGE, END
import tkinter as tk


# GUI helper function
def create_dropdown(parent, dropdown_menu):
	return ttk.Combobox(
		parent,
		state='readonly',
		values=dropdown_menu,
		width=30
		)

def clear_frame(frame):
	for item in frame.winfo_children():
		item.destroy()

# Display Frontpage
def display_frontpage():
	# Helper function for frontpage actions
	def frontpage_selection(event):
		# Helper function for choice 1
		def choice1_button_response():
			user_input = input_box.get(1.0, END)
			print(user_input)
			messagebox.showinfo(
					title='Testing!',
					message=f"User entered {user_input}"
					)

		# Helper function for choice 2
		def choice2_dropdown(event):
			choice = frame2_dropdown.get()

			if choice == 'I still cannot choose!':
				messagebox.showinfo(
						title='Selection',
						message=f"Let's try MaCallan first!"
						)
				# Clear out all page2 instructions
				headline_secondchoice.config(text='')
				clear_frame(frame_page2_input)
			else:
				def flavour_choice(event):
					choice_flavour = frame2_dropdown.get()
					choice_strength = frame3_dropdown.get()
					messagebox.showinfo(
						title='Testing!',
						message=f"User entered {choice_strength} {choice_flavour}"
						)

				clear_frame(frame3)
				frame3_question = tk.Frame(frame3)
				frame3_dropdown_frame = tk.Frame(frame3)

				question3 = tk.Label(master=frame3_question, text='Please select a flavour:')
				question3.pack()

				frame3_dropdown = create_dropdown(frame3, strengthlist)
				# Bind and Pack the changes
				frame3_dropdown.bind("<<ComboboxSelected>>", flavour_choice)
				
				frame3_question.pack()
				frame3_dropdown.pack()
				frame3_dropdown_frame.pack()


		selection = frontpage_dropdown.get()
		choice = int(selection[0])
		clear_frame(frame_page2_input)

		if choice == 1:
			# Show instruction
			headline_secondchoice.config(text='Please enter your favourite whisky:')
			input_box = tk.Text(frame_page2_input, height=1, width=20,
				relief=RIDGE, borderwidth=5)
			input_box.pack()

			# Create children frames and function
			frame2_button_frame = tk.Frame(frame_page2_input)
			frame3 = tk.Frame(frame_page2_input)
			frame2_button = tk.Button(frame2_button_frame, text='Submit', command=choice1_button_response)
			frame2_button.pack()
			frame2_button_frame.pack()
			frame3.pack()

		if choice == 2:
			# Show instruction
			headline_secondchoice.config(text='Please select your preferred flavour in the following options:')
			# Layout all GUI objects
			frame2_dropdown_frame = tk.Frame(frame_page2_input)
			frame3 = tk.Frame(frame_page2_input)
			frame2_dropdown = create_dropdown(frame2_dropdown_frame, whisky_features)
			# Bind and Pack the changes
			frame2_dropdown.bind("<<ComboboxSelected>>", choice2_dropdown)
			frame2_dropdown.pack()
			frame2_dropdown_frame.pack()
			frame3.pack()

		elif choice == 3:
			headline_secondchoice.config(text='')
			messagebox.showinfo(
				title='Selection',
				message=f"You may try MaCallan"
				)
	
	# Define all base Frames
	frame_main = tk.Frame()
	frame_frontpage_question = tk.Frame()
	frame_frontpage_dropdown = tk.Frame()
	frame_page2_question = tk.Frame()
	frame_page2_input = tk.Frame()

	# Headline
	headline = tk.Label(master=frame_main, text='Welcome to the Whisky Recommender')
	headline.pack()

	# Show instruction (Question 1)
	frontpage_question = tk.Label(master=frame_frontpage_question,
		text='Please select the following option:')
	frontpage_question.pack()

	# Create dropdown list for Question 1
	frontpage_dropdown_menu = ['1 - Start by entering whisky name', '2 - Start by choosing flavor','3 - No idea where to start']
	frontpage_dropdown = create_dropdown(frame_frontpage_dropdown, frontpage_dropdown_menu)
	frontpage_dropdown.bind("<<ComboboxSelected>>", frontpage_selection)
	frontpage_dropdown.pack()


	# Create empty box for follow up instruction (Question 2)
	headline_secondchoice = tk.Label(master=frame_page2_question, text='')
	headline_secondchoice.pack()

	# Bind and Pack the changes
	frame_main.pack()
	frame_frontpage_question.pack()
	frame_frontpage_dropdown.pack()
	frame_page2_question.pack()
	frame_page2_input.pack()

# List for choice 2
whisky_features = ['Body','Sweetness','Smoky','Medicinal','Tobacco',
                   'Honey','Spicy','Winey','Nutty','Malty','Fruity',
                   'Floral','I still cannot choose!']
strengthlist = ['None','Light','Medium','Strong','Very strong']
