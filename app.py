from tkinter import *
import random

class App:
    def __init__(self, master): # "master" is the main window
        # Frame (like a container) for the buttons
        top_frame = Frame(master)
        top_frame.pack()

        # Buttons
        self.rock_btn = Button(top_frame, text = 'Rock', padx = 25, pady = 15, bg = 'spring green',
        font = 'system 18', command = self.chose_rock)
        self.rock_btn.grid(row = 0, column = 0, padx = 35, pady = 55)

        self.paper_btn = Button(top_frame, text = 'Paper', padx = 25, pady = 15, bg = 'orchid1',
        font = 'system 18', command = self.chose_paper)
        self.paper_btn.grid(row = 0, column = 1, padx = 35, pady = 55)

        self.scissors_btn = Button(top_frame, text = 'Scissors', padx = 25, pady = 15, bg = 'navajo white',
        font = 'system 18', command = self.chose_scissors)
        self.scissors_btn.grid(row = 0, column = 2, padx = 35, pady = 55)

        # Second frame for the user and computer results
        middle_frame = Frame(master)
        middle_frame.pack()

        self.user_choice_lbl = Label(middle_frame, text = 'User\'s choice was: ?', padx = 35, pady = 35,
        font = 'system 16')
        self.user_choice_lbl.grid(row = 0, column = 0)

        self.computer_choice_lbl = Label(middle_frame, text = 'Computer\'s choice was: ?', padx = 35, pady = 35,
        font = 'system 16')
        self.computer_choice_lbl.grid(row = 0, column = 1)

        # Third frame for the winner
        bottom_frame = Frame(master)
        bottom_frame.pack()

        self.winner = Label(bottom_frame, text = 'The winner is... 😓', padx = 35, pady = 35,
        font = 'system 26')
        self.winner.grid(row = 0, columnspan = 3)

    # Functions go here
    def chose_rock(self):
        self.play('Rock')

    def chose_paper(self):
        self.play('Paper')

    def chose_scissors(self):
        self.play('Scissors')

    def play(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)
        has_won = True

        # To update the labels
        self.user_choice_lbl.config(text = f'User\'s choice was: {user_choice}')
        self.computer_choice_lbl.config(text = f'Computer\'s choice was: {computer_choice}')

        # Combinations
        if user_choice == 'Rock' and computer_choice == 'Paper':
            has_won = False
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            has_won = True
        elif user_choice == 'Paper' and computer_choice == 'Scissors':
            has_won = False
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            has_won = True
        elif user_choice == 'Rock' and computer_choice == 'Scissors':
            has_won = True
        elif user_choice == 'Scissors' and computer_choice == 'Rock':
            has_won = False
        elif user_choice == computer_choice:
            has_won = None

        if has_won == True:
            self.winner.config(text = 'The winner is... You! 😍', fg = 'green2')
        elif has_won == False:
            self.winner.config(text = 'The winner is... Me! 😥', fg = 'indianred1')
        else:
            self.winner.config(text = 'The game was a draw! 😲', fg = 'orange')

root = Tk()
root.title('Rock Paper Scissors')
root.geometry('1000x500')
root.resizable(0, 0) # Disables maximise

# Create an object for the class
obj = App(root)

root.mainloop()
