from tkinter import *
from tkinter import massagebox


def click():
    massagebox.showinfo(title='this is an info massage box',

                        massage='you are a man ')
    massagebox.showwarning(title='Waring',

                           massage='you  have a virus ')


window = Tk()
button = Button(window, command=click, text='click me ')
button.pack()
window.mainloop()
