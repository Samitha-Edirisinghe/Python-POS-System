from tkinter import *

#----------------------------------------------------

class MyLabel():

    def __init__(self, home, txt, r, c, px=None, py=None, sticky=W, fn="Rockwell", color='#ADD8E6', cp=None, txtvar=None):

        self.home=home
        self.txt=txt
        self.r=r
        self.c=c
        self.px=px
        self.py=py
        self.sticky = sticky
        self.fn=fn
        self.color=color
        self.cp=cp
        self.txtvar = txtvar

    def myL(self):

        lbl=Label(self.home, text=self.txt, textvariable=self.txtvar)
        lbl.grid(row=self.r, column=self.c, columnspan=self.cp, padx=self.px, pady=self.py, sticky=self.sticky)
        lbl.config(bg=self.color, font=self.fn)

#----------------------------------------------------

class MyEntry():

    def __init__(self, home, r, c, w=None, px=None, py=None, st=None, var=None, fn="arial", bg="#CBE2EF"):

        self.home=home
        self.r=r
        self.c=c
        self.w=w
        self.px=px
        self.py=py
        self.st=st
        self.var = var
        self.fn=fn
        self.bg = bg
        self.ent=Entry(home)

    def config(self):

        self.ent.grid(row=self.r, column=self.c, padx=self.px, pady=self.py, sticky=self.st)
        self.ent.config(text=self.var, font=self.fn, width=self.w, bg=self.bg)

    def show(self):
        return self.ent.get()

    def get(self):

        return (self.ent.get())


#-------------------------------------------------------


class MyButton():

    def __init__(self, home, txt, command, r, c, w, px=None, py=None, st=None):

        self.home = home
        self.txt = txt
        self.command=command
        self.r = r
        self.c = c
        self.w = w
        self.px=px
        self.py=py
        self.st=st

    def myB(self):

        btn=Button(self.home, text=self.txt, command=self.command, width=self.w, bg="#789AFF")
        btn.grid(row=self.r, column=self.c, padx=self.px, pady=self.py, sticky=self.st)
        #btn.configure(bg=self.co)

#-------------------------------------------------------

"""
class MyListbox():

    def __init__(self, home, r, c, rp, px, py):

        self.home=home
        self.r=r
        self.c=c
        self.rp=rp
        self.px=px
        self.py=py

    def myLB(self):

        lstbox=Listbox(self.home)
        lstbox.grid(row=self.r, column=self.c, rowspan=self.rp, padx=self.px, pady=self.py)
        lstbox.config(bg="#ADC8F6")
"""
