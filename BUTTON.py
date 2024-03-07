from tkinter import *

def click():
    print("clicked")


window = Tk()

button = Button(window,
                text="click here",
                command=click,
                font=("Georgia",100))
button.pack()

window.mainloop()