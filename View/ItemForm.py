from tkinter import *
from tkinter import ttk
from Controller import ItemController
from tkinter import messagebox
import gadget

class ItemForm():

        def __init__(self, home):

            home.config(bg="#ADD8E6")

            #--------------------------------------------------
            #Defs
            #--------------------------------------------------

            idlst=[]

            def load(event=None):

                try:
                    lbData.delete(0,END)
                except:
                    None
                itmCon=ItemController.ItemController()
                data=itmCon.load()
                for i in data:
                    lbData.insert(END,(str(i[0])+" - "+i[1]))
                    idlst.append(i[0])

            def clicked(event):
                try:
                    lst=event.widget
                    num=lst.curselection()[0]
                    value=lst.get(num)
                    S_ID=value.split(" - ")[0]

                    S_Name=value.split(" - ")[1]
                    var1.set(S_ID)
                    var2.set(S_Name)

                    itmCon=ItemController.ItemController(S_ID)
                    itmCon.getpr()
                    Pr=itmCon.getpr()
                    var3.set(Pr)
                except:
                    None

            def Delete():
                try:
                    id = txtID.get()
                    name = txtNm.get()
                    prz = txtPr.get()

                    itmCon = ItemController.ItemController(id, name, prz)
                    itmCon.delete()
                    messagebox._show("Done!", "The record deleted\nsuccessfully")

                except:
                    messagebox._show("Oops!", "Something went wrong\nplease try again")

            def Save():

                try:
                    id = txtID.get()
                    name = txtNm.get()
                    prz = txtPr.get()

                    itmCon = ItemController.ItemController(id, name, prz)

                    if int(id) not in idlst:

                        itmCon.save()
                        messagebox._show("Done!", "New record saved\nsuccessfully")

                    else:

                        itmCon.update()
                        messagebox._show("Done!", "The record updated\nsuccessfully")

                except:
                    messagebox._show("Oops!", "Something went wrong\nplease try again")

            #--------------------------------------------------------------------------
            #User Intrface
            #--------------------------------------------------------------------------

            lblbnr1=gadget.MyLabel(home, "ITEM REGISTRATION", 0, 0, None, None, W+E, "Algerian", "#77AEFD", 2)
            lblbnr1.myL()

            lblbnr1=gadget.MyLabel(home, " ", 0, 2, None, None, W+E, "Algerian", "#77AEFD")
            lblbnr1.myL()

            lblId=gadget.MyLabel(home, "Catogary :- ", 1, 0, 3, None, E, "Centaur")
            lblId.myL()

            #------------------------------------------------

            itmCon=ItemController.ItemController()
            catLst=itmCon.catlist()

            cmbCat = ttk.Combobox(home, values=catLst, width=12, state="readonly")
            cmbCat.grid(row=1, column=1)

            #------------------------------------------------

            lblId=gadget.MyLabel(home, "ID", 2, 0, 10)
            lblId.myL()

            lbldot1=gadget.MyLabel(home, ":", 2, 1, None, None, None, "Broadway")
            lbldot1.myL()

            var1=StringVar()
            txtID=gadget.MyEntry(home, 2, 2, 12, 10, 5, W, var1, None)
            txtID.config()

            lblNm=gadget.MyLabel(home, "Name", 3, 0, 10)
            lblNm.myL()

            lbldot2=gadget.MyLabel(home, ":", 3, 1, None, None, None, "Broadway")
            lbldot2.myL()

            var2=StringVar()
            txtNm=gadget.MyEntry(home, 3, 2, 12, 10, 10, W, var2, None)
            txtNm.config()

            lblPr=gadget.MyLabel(home, "Price", 4, 0, 10)
            lblPr.myL()

            lbldot3=gadget.MyLabel(home, ":", 4, 1, None, None, None, "Broadway")
            lbldot3.myL()

            var3=StringVar()
            txtPr=gadget.MyEntry(home, 4, 2, 12, 10, 4, W, var3, None)
            txtPr.config()

            btnDEL=gadget.MyButton(home, "Delete", Delete, 5, 0, 7, 8, 8, E)
            btnDEL.myB()

            btnSAV=gadget.MyButton(home, "Save", Save, 5, 2, 7, 5, 8, W)
            btnSAV.myB()

            scrollbar = Scrollbar(home)
            scrollbar.grid(row=0, column=4, rowspan=13, sticky=N + S)

            lbData=Listbox(home, width=18, height=12, yscrollcommand=scrollbar.set)
            lbData.grid(row=0, column=3, rowspan=20, sticky=N+E)
            lbData.config(bg="#ADC8F6")
            scrollbar.config(command=lbData.yview)

            lbData.bind('<<ListboxSelect>>', clicked)
            home.bind('<Configure>', load)

            #-----------------------------------------------------------------------

            home.mainloop()