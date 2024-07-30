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
    # Helper function for frontpage actions
    def frontpage_selection(event):
    # display_frontpage core operations begins here
        selection = frontpage_dropdown.get()
        choice = int(selection[0])
        clear_frame(frame_page2_input)

        if choice == 1:
            # Show instruction
            # headline_secondchoice.config(
            #     text='Please enter your favourite whisky:')
            input_box = tk.Text(frame_page2_input, height=1, width=20,
                                relief=RIDGE, borderwidth=5)
            input_box.pack()

            # Create children frames and function
            # frame2_button_frame = tk.Frame(frame_page2_input)
            frame3 = tk.Frame(frame_page2_input)
            # frame2_button.pack()
            # frame2_button_frame.pack()
            frame3.pack()


            # Delete later, temp message box
            messagebox.showinfo(
                title='Selection',
                message=f"Feature coming soon!"
            )


        if choice == 2:
            # headline_secondchoice.config(text='')
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
    frontpage_dropdown.bind("<<ComboboxSelected>>", frontpage_selection)
    frontpage_dropdown.pack()

    # Bind and Pack the changes
    frame_main.pack()
    frame_frontpage_question.pack()
    frame_frontpage_dropdown.pack()
