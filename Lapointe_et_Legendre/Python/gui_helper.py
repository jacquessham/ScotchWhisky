from tkinter import messagebox, ttk, RIDGE, END, Entry, NSEW
import tkinter as tk


# GUI helper function
def create_dropdown(parent, dropdown_menu):
    return ttk.Combobox(
        parent,
        state='readonly',
        values=dropdown_menu,
        width=30
    )

# Clear frame after some user selection
def clear_frame(frame):
    for item in frame.winfo_children():
        item.destroy()

# Display Frontpage
def display_frontpage():
    # Define all base Frames
    frame_main = tk.Frame()
    frame_frontpage_question = tk.Frame()
    frame_frontpage_dropdown = tk.Frame()
    frame_page2_question = tk.Frame()
    frame_page2_input = tk.Frame()


    # Headline
    headline = tk.Label(master=frame_main,
                        text='Welcome to the Whisky Recommender')
    headline.pack()

    # Show instruction (Question 1)
    frontpage_question = tk.Label(master=frame_frontpage_question,
                                  text='Please select the following option:')
    frontpage_question.pack()

    # Create dropdown list for Question 1
    frontpage_dropdown_menu = ['1 - Pick a distillery',
                               '2 - No idea where to start']
    frontpage_dropdown = create_dropdown(frame_frontpage_dropdown,
                                         frontpage_dropdown_menu)
    # Will come back later
    # frontpage_dropdown.bind("<<ComboboxSelected>>", frontpage_selection)
    frontpage_dropdown.pack()

    # Bind and Pack the changes
    frame_main.pack()
    frame_frontpage_question.pack()
    frame_frontpage_dropdown.pack()
