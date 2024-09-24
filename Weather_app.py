from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk 
from tkinter import messagebox
import openpyxl,xlrd
from openpyxl import workbook
import pathlib



root=Tk()
root.title("Data Entry")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg="#13313b")

#icon 
icon_image=PhotoImage(file="logo.png")
root.iconphoto(False,icon_image)



#heading 
Label(root,text="Now fill out this Entry Form",font="arial 13",bg="#326273",fg="#fff").place(x=20,y=20)

#label1
Label(root,text='Name:',font=23,bg="#326273",fg="#fff").place(x=50,y=100)
Label(root,text='Contact No:',font=23,bg="#326273",fg="#fff").place(x=50,y=150)
Label(root,text='Age:',font=23,bg="#326273",fg="#fff").place(x=50,y=200)
Label(root,text='Gender:',font=23,bg="#326273",fg="#fff").place(x=370,y=200)
Label(root,text='Address:',font=23,bg="#326273",fg="#fff").place(x=50,y=250)

#Entry
namevalue=StringVar()
contactvalue=StringVar()
agevalue=StringVar()

nameEntry=Entry(root ,textvariable=namevalue,width=45,bd=2,font=20)
contactEntry=Entry(root ,textvariable=contactvalue,width=45,bd=2,font=20)
ageEntry=Entry(root ,textvariable=agevalue,width=45,bd=2,font=20)

nameEntry.place(x=200,y=100)
contactEntry.place(x=200,y=150)
ageEntry.place(x=200,y=200)

root.mainloop()
