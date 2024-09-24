from tkinter import *


def click():
    print("You clicked the button!")


window = Tk()
Button = Button(window, text="clik me!",
                command=click, font=("comics sans", 30),
                fg="#42f2f5",
                bg="black"
                )
Button.pack()
window.mainloop()
