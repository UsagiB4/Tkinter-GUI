from tkinter import *

root = Tk()

usr_input = Entry(root, width=50, borderwidth=5, bg='#314559', fg='#c0ff33')
usr_input.insert(0, "Hay can you give a input?")


def txt_input():
    input_txt = usr_input.get()
    show_inp = Label(root, text=input_txt)
    show_inp.pack()


inp_button = Button(root, text='Click to send', bg='#1b3147', fg='#f9dd6f', padx=10, pady=10, command=txt_input)
simpleLabel = Label(root, text="Input here", bg='black', fg='white')


simpleLabel.pack()
usr_input.pack()
inp_button.pack()
root.mainloop()
