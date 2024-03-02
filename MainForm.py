from tkinter import *
from View import ItemForm
from View import CatogaryForm
from View import SalesForm
from View import ReportViewer

#---------------------------------------------------

def catogary():
    remove()
    CatogaryForm.CatogaryForm(frame)

#---------------------------------------------------

def item():
    remove()
    ItemForm.ItemForm(frame)

#---------------------------------------------------

def sales():
    remove()
    SalesForm.SalesForm(frame)

#---------------------------------------------------

def report():
    remove()
    ReportViewer.ReportViewer(frame)

#---------------------------------------------------

def remove():
    for ged in frame.winfo_children():
        ged.destroy()

#---------------------------------------------------

home=Tk()
home.title("Shopping System - v1.0.2")
home.geometry("1201x664")
home.state("zoomed")
home.config(bg="#C0C0C0")

frame=Frame(home)
frame.configure(background="#c0c0c0")
frame.pack()

menubar=Menu(home)
home.config(menu=menubar)

register = Menu(menubar, tearoff=0)
register.config(font='Verdana')

menubar.add_cascade(label="Register", menu=register)
register.add_command(label="Catogary", command=catogary)
register.add_command(label="Item", command=item)

menubar.add_command(label='Sales', command=sales)

menubar.add_command(label='Report', command=report)

#---------------------------------------------------

home.mainloop()
