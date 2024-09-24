# function is block of code
from tkinter import Tk


def say_hi(name, age):
    print("Hello "+name, "you are "+str(age))


print("top")
say_hi("Sadman", 25)
say_hi("Nafiz", 70)
print("Bottom")


def say_by(Id, sec):
    print("my id is "+Id, "And sec:"+sec)


print("Nafiz")
window = Tk()
