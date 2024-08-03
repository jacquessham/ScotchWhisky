from tkinter import messagebox, ttk, RIDGE, END, Entry, NSEW
import tkinter as tk
from recommendation_flow import *


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

# Helper function to display a table
def plot_table(root, recommendations, num2dis):
    height = len(recommendations)//4 + 1

    if len(recommendations) > 0:
        # Create a children frame
        subframe_message = tk.Frame(root)

        # Show the message
        message = tk.Label(master=subframe_message,
                           text='Here are our recommendation:')
        message.pack()
        subframe_message.pack()

        # Show the table
        subframe_recommendation = tk.Frame(root)

        """
        ## This block can be used when users does not care about distance
        for i in range(height):
            for j in range(4):
                i_recommendation = i*4+j
                if i_recommendation < len(recommendations):
                    e = Entry(subframe_recommention, relief=RIDGE)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, 
                        num2dis[recommendations[i_recommendation][0]])
        """

        # This block can be used when displaying distance is needed
        for i in range(len(recommendations)+1):
            if i == 0:
                e0 = Entry(subframe_recommendation, relief=RIDGE)
                e0.grid(row=i, column=0, sticky=NSEW)
                e0.insert(END, 'Rank')
                e1 = Entry(subframe_recommendation, relief=RIDGE)
                e1.grid(row=i, column=1, sticky=NSEW)
                e1.insert(END, 'Distillery Name')
                e2 = Entry(subframe_recommendation, relief=RIDGE)
                e2.grid(row=i, column=2, sticky=NSEW)
                e2.insert(END, 'Distance')
            else:
                e0 = Entry(subframe_recommendation, relief=RIDGE)
                e0.grid(row=i, column=0, sticky=NSEW)
                e0.insert(END,i)
                e1 = Entry(subframe_recommendation, relief=RIDGE)
                e1.grid(row=i, column=1, sticky=NSEW)
                e1.insert(END, num2dis[recommendations[i-1][0]])
                e2 = Entry(subframe_recommendation, relief=RIDGE)
                e2.grid(row=i, column=2, sticky=NSEW)
                e2.insert(END, recommendations[i-1][1])

        subframe_recommendation.pack()


# Display Frontpage
def display_frontpage(results, num2dis):
    # Helper function for frontpage actions
    def frontpage_selection(event):
    # display_frontpage core operations begins here
        selection = frontpage_dropdown.get()
        choice = int(selection[0])
        clear_frame(frame_page2_question)
        clear_frame(frame_page2_input)

        # When users want to pick a whisky to start with
        if choice == 1:
            # Helper function
            def q2_selection(event):
                clear_frame(frame2)
                q2_distillery = q2_dropdown.get()
                q2_choice = int(q2_distillery[0])-1

                # Get a list of recommendation
                recommendations = get_recommendation(results, num2dis, 
                    q2_choice, False, False)

                # Pack all setups
                space = tk.Label(master=frame2, text='')
                space.pack() # Add space to be consistent with choice==2
                plot_table(frame2, recommendations, num2dis)

            
            # UI Display here for choice 1
            # Show instruction
            headline_secondchoice = tk.Label(master=frame_page2_input, 
                text='Please select your favourite whisky:')
            headline_secondchoice.pack()
            
            # Create children frames and function
            frame2 = tk.Frame(frame_page2_input)
            # Dropdown list here
            # Create dropdown list for Question 2
            q2_dropdown_menu = [f'{dis_num+1}: {num2dis[dis_num]}' 
                    for dis_num in num2dis.keys()]
            q2_dropdown = create_dropdown(frame_page2_input,
                                          q2_dropdown_menu)
            frame2 = tk.Frame(frame_page2_input)
            q2_dropdown.bind("<<ComboboxSelected>>", q2_selection)
            

            # Pack all setups before user's q2 selection
            headline_secondchoice.pack()
            frame_page2_question.pack()
            q2_dropdown.pack()
            frame2.pack()
            frame_page2_input.pack()


        # When user wants the program pick a whisky for them
        if choice == 2:
            # Notify user through pop up text box
            messagebox.showinfo(
                title='Selection',
                message=f"You may try MaCallan"
            )

            # num_MaCallan comes from recommendation_flow.py
            q2_choice = num_MaCallan 
            # Get a list of recommendation
            recommendations = get_recommendation(results, num2dis, q2_choice, 
                False, False)

            # Pack all setups
            frame2 = tk.Frame(frame_page2_input)
            plot_table(frame2, recommendations, num2dis)
            # Generate a recommmendation here
            frame2.pack()
            frame_page2_input.pack()

        # Ending Helper function


    # Define all base Frames
    frame_main = tk.Frame()
    frame_frontpage_question = tk.Frame()
    frame_frontpage_dropdown = tk.Frame()
    frame_page2_question = tk.Frame()
    frame_page2_input = tk.Frame()
    

    # Base UI structure are built here
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

