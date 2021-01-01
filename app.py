from tkinter import *

class App:
        def __init__(self, master): # "master" is the main window
            # Frame (like a container) for the buttons
            topFrame = Frame(master)
            topFrame.pack()

            # Buttons
            self.rockBtn = Button(topFrame, text = 'Rock', padx = 25, pady = 15, bg = 'spring green',
            font = 'system 18', command = self.play)
            self.rockBtn.grid(row = 0, column = 0, padx = 35, pady = 35)

            self.paperBtn = Button(topFrame, text = 'Paper', padx = 25, pady = 15, bg = 'orchid1',
            font = 'system 18', command = self.play)
            self.paperBtn.grid(row = 0, column = 1, padx = 35, pady = 35)

            self.scissorsBtn = Button(topFrame, text = 'Scissors', padx = 25, pady = 15, bg = 'navajo white',
            font = 'system 18', command = self.play)
            self.scissorsBtn.grid(row = 0, column = 2, padx = 35, pady = 35)

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
        def play(self):
            print('Don\'t click me')

            # To update the labels
            self.userChoiceLbl.config()
            self.computerChoiceLbl.config()
            self.winner.config()

root = Tk()
root.title('Rock Paper Scissors')
root.geometry('1000x500')

# Create an object for the class
obj = App(root)

root.mainloop()
