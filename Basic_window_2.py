from tkinter import*

root = Tk()

topFrame = Frame(root)
root.title("Wallhack")
root.geometry("500x500")

#pack command places the windon on the screen
#by default pack command sets the window on top.
topFrame.pack()


bottomFrame = Frame(root)
#puts the fram on the bottom, because it is on top by default
bottomFrame.pack(side=BOTTOM)

#creation of button
#button syntax is button(where, text="", fg="color")
#fg stands for foreground
button1 = Button(topFrame, text="BUTTON 1", fg="red",)
button2 = Button(topFrame, text="BUTTON 2", fg="blue")
button3 = Button(topFrame, text="BUTTON 3", fg="violet")
button4 = Button(bottomFrame, text="BUTTON 4", fg="green")


#displays the button on the screen
#packing packs them on top of another
#new packs parameter here
#LEFT must be capitalized, and puts the thing on far left
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)



root.mainloop()
