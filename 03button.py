from tkinter import *

root = Tk()


def a_click():
    a_label = Label(root, text="A click has happened")
    a_label.pack()


simpleLabel = Label(root, text="Just simple Text here")

simpleButton = Button(root, text="Click here", padx=50, pady=20, command=a_click, fg='red', bg='#c0ff33')
simpleButton.pack()
simpleLabel.pack()
root.mainloop()
