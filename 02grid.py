from tkinter import *

root = Tk()  # creating root widget

label = Label(root, text="Hello world")  # label
labelA = Label(root, text="Buy buy world")  # another label
labelB = Label(root, text="Row 1 column 2")
label.grid(row=0, column=0)  # first row and first column
labelA.grid(row=1, column=0)  # second row in the first column
labelB.grid(row=0, column=1)  # first row and second column

root.mainloop()
