from tkinter import *

root = Tk()

simpleLabel = Label(root, text="Just simple Text here")


simpleButton = Button(root, text="Click here")
simpleButton.grid(row=0, column=0)
simpleLabel.grid(row=2, column=0)
root.mainloop()
