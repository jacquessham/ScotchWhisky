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
        subframe_recommention = tk.Frame(root)

        for i in range(height):
            for j in range(4):
                i_recommendation = i*4+j
                if i_recommendation < len(recommendations):
                    e = Entry(subframe_recommention, relief=RIDGE)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, 
                        num2dis[recommendations[i_recommendation][0]])
        subframe_recommention.pack()


# Display Frontpage
def display_frontpage(results, num2dis):
    # Helper function for frontpage actions
    def frontpage_selection(event):
    # display_frontpage core operations begins here
        selection = frontpage_dropdown.get()
        choice = int(selection[0])
        clear_frame(frame_page2_question)
        clear_frame(frame_page2_input)

        # Create empty box for follow up instruction (Question 2)
        headline_secondchoice = tk.Label(master=frame_page2_question, text='')
        headline_secondchoice.pack()

        if choice == 1:
            # Helper function
            def q2_selection(event):
                clear_frame(frame2)
                q2_distillery = q2_dropdown.get()
                q2_choice = int(q2_distillery[0])-1
                print(q2_choice)
                print(num2dis[q2_choice])

                recommendations = get_recommendation(results, num2dis, 
                    q2_choice, False, False)
                print(recommendations)

                # Pack all setups
                space = tk.Label(master=frame2, text='')
                space.pack() # Add space to be consistent with choice==2
                plot_table(frame2, recommendations, num2dis)
                # Generate a recommmendation here
                frame2.pack()
                frame_page2_input.pack()

            # Ending Helper function


            # Show instruction
            headline_secondchoice.config(
                text='Please select your favourite whisky:')
            
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
            frame_page2_question.pack()
            headline_secondchoice.pack()
            q2_dropdown.pack()
            frame2.pack()
            frame_page2_input.pack()


        if choice == 2:
            # headline_secondchoice.config(text='')
            messagebox.showinfo(
                title='Selection',
                message=f"You may try MaCallan"
            )

            q2_choice = num_MaCallan 
            print(q2_choice)
            print(num2dis[q2_choice])
            recommendations = get_recommendation(results, num2dis, q2_choice, 
                False, False)
            print(recommendations)

            # Pack all setups
            frame2 = tk.Frame(frame_page2_input)
            plot_table(frame2, recommendations, num2dis)
            # Generate a recommmendation here
            frame2.pack()
            frame_page2_input.pack()


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

