#imports the library that supports window creation
from tkinter import*

#Root is the blank window
root = Tk()

#Labels
flashcard = Label(root, text="Chicken Feet Gang")

#pack means just put the window somewhere
flashcard.pack()

#sets the window continously running
#basically it makes the scren stay
root.mainloop()
