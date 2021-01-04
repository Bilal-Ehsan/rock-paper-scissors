from tkinter import *
import random

class App:
    def __init__(self, master): # "master" is the main window
        # Frame (like a container) for the buttons
        topFrame = Frame(master)
        topFrame.pack()

        # Buttons
        self.rockBtn = Button(topFrame, text = 'Rock', padx = 25, pady = 15, bg = 'spring green',
        font = 'system 18', command = self.choseRock)
        self.rockBtn.grid(row = 0, column = 0, padx = 35, pady = 55)

        self.paperBtn = Button(topFrame, text = 'Paper', padx = 25, pady = 15, bg = 'orchid1',
        font = 'system 18', command = self.chosePaper)
        self.paperBtn.grid(row = 0, column = 1, padx = 35, pady = 55)

        self.scissorsBtn = Button(topFrame, text = 'Scissors', padx = 25, pady = 15, bg = 'navajo white',
        font = 'system 18', command = self.choseScissors)
        self.scissorsBtn.grid(row = 0, column = 2, padx = 35, pady = 55)

        # Second frame for the user and computer results
        middleFrame = Frame(master)
        middleFrame.pack()

        self.userChoiceLbl = Label(middleFrame, text = 'User\'s choice was: ?', padx = 35, pady = 35,
        font = 'system 16')
        self.userChoiceLbl.grid(row = 0, column = 0)

        self.computerChoiceLbl = Label(middleFrame, text = 'Computer\'s choice was: ?', padx = 35, pady = 35,
        font = 'system 16')
        self.computerChoiceLbl.grid(row = 0, column = 1)

        # Third frame for the winner
        bottomFrame = Frame(master)
        bottomFrame.pack()

        self.winner = Label(bottomFrame, text = 'The winner is... 😓', padx = 35, pady = 35,
        font = 'system 26')
        self.winner.grid(row = 0, columnspan = 3)

    # Functions go here
    def choseRock(self):
        self.play('Rock')

    def chosePaper(self):
        self.play('Paper')

    def choseScissors(self):
        self.play('Scissors')

    def play(self, userChoice):
        choices = ['rock', 'paper', 'scissors']
        computerChoice = random.choice(choices)
        hasWon = True

        # To update the labels
        self.userChoiceLbl.config(text = f'User\'s choice was: {userChoice}')
        self.computerChoiceLbl.config(text = f'Computer\'s choice was: {computerChoice}')

        # Combinations
        if userChoice == 'Rock' and computerChoice == 'Paper':
            hasWon = False
        elif userChoice == 'Paper' and computerChoice == 'Rock':
            hasWon = True
        elif userChoice == 'Paper' and computerChoice == 'Scissors':
            hasWon = False
        elif userChoice == 'Scissors' and computerChoice == 'Paper':
            hasWon = True
        elif userChoice == 'Rock' and computerChoice == 'Scissors':
            hasWon = True
        elif userChoice == 'Scissors' and computerChoice == 'Rock':
            hasWon = False
        elif userChoice == computerChoice:
            hasWon = None

        if hasWon == True:
            self.winner.config(text = 'The winner is... You! 😍')
        elif hasWon == False:
            self.winner.config(text = 'The winner is... Me! 😥')
        else:
            self.winner.config(text = 'The game was a draw! 😲')

root = Tk()
root.title('Rock Paper Scissors')
root.geometry('1000x500')
root.resizable(0, 0) # Disables maximise

# Create an object for the class
obj = App(root)

root.mainloop()
