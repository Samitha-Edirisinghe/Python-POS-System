from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Controller import ItemController
from Controller import SalesController
import time
import gadget

tot = 0

class SalesForm():

    def __init__(self, home):

        home.config(bg="#ADD8E6")

        def load(event=None):

            try:
                lbData.delete(0, END)
            except:
                None
            itmCon = ItemController.ItemController()
            data = itmCon.load()
            for i in data:
                try:
                    lbData.insert(END, (str(i[0]) + " - " + i[1]))
                except:
                    None

            nxtId=itmCon.nxtid()[0][0]
            Nid.set(nxtId)

        def clicked(event):

            lst = event.widget
            try:
                num = lst.curselection()[0]
                value = lst.get(num)
                S_ID = value.split(" - ")[0]
                S_Name = value.split(" - ")[1]
                itmCon = ItemController.ItemController(S_ID)
                itmCon.getpr()
                Pr = itmCon.getpr()
                varPrz.set("Rs. {}".format(Pr))
                varId.set(S_ID)
                varName.set(S_Name)
            except:
                None
            txtQty.focus()

        def add():

            txtId.focus()
            global tot
            g_id = txtId.get()
            try:
                g_qty = float(txtQty.get())
            except:
                messagebox._show("Wait","Invalid quantity")
                return
            saleCon = SalesController.SalesController(txtId.get())

            val= saleCon.addItem()
            if (val == 0):
                messagebox._show("Error","Invalid Item ID")
                txtId.delete(0, END)
                txtId.focus()

            else:
                g_name = val[0][1]
                try:
                    g_dis = float(txtDis.get())
                except:
                    messagebox._show("Wait", "Invalid discount")
                    return
                g_price = float(val[0][2]) - float(txtDis.get())
                value = (float(val[0][2])-g_dis)*g_qty
                varVal.set(value)
                tvData.insert('', 'end', values=[g_id,g_name,g_price,g_qty,value])

                txtId.delete(0, END)
                varDis.set(0)
                txtQty.delete(0, END)
                tot = tot + value
                strTotal.set("Rs. {}".format(tot))

        def key_evt(event):

            if (event.keycode == 13):
                add()

        def key_evt_src(event):

            nm_lst = []
            itmCon = ItemController.ItemController()
            data = itmCon.load()
            for i in data:
                nm_lst.append(i[1])
            ch=event.char
            chkl=0
            sel_lst=[]
            while len(nm_lst) > chkl:
                if (nm_lst[chkl][0].upper() == ch.upper()):
                    sel_lst.append(nm_lst[chkl])
                elif event.keycode == 8:
                    lbData.delete(0, END)
                    for i in data:
                        lbData.insert(END, (str(i[0]) + " - " + i[1]))
                    return
                chkl += 1

            lbData.delete(0, END)
            for i in data:
                if i[1] in sel_lst:
                    lbData.insert(END, (str(i[0]) + " - " + i[1]))

        def for_evt(event):
            g_dis2 = txtLDis.get()
            netValue = tot - float(g_dis2)
            netAmnt.set("Rs. {}".format(netValue))
            return netAmnt

        def key_dis(event):
            if event.keycode == 13:
                for_evt(event)

        def dets(event):

            try:
                saleCon = SalesController.SalesController(txtId.get())
                val = saleCon.addItem()
                g_name = val[0][1]
                g_price = val[0][2]
                varName.set(g_name)
                varPrz.set("Rs. {}".format(g_price))
            except:
                None

        def save():

            global tot
            try:
                treeall = []
                for child in tvData.get_children():
                    treeall.append(tvData.item(child)["values"])

                slsCon = SalesController.SalesController(None, txtBind.get(), date, txtLDis.get(), None, None, txtQty.get(), treeall)
                slsCon.saveSum()
            except:
                None

            for i in tvData.get_children():
                tvData.delete(i)
            strTotal.set("Rs. 0.0")
            varLDis.set(0)
            netAmnt.set("Rs. 0.0")
            varName.set("(no_data)")
            varPrz.set("(no_data)")
            varVal.set("(no_data)")
            try:
                if (treeall[0][0] > 0):
                    itmCon = ItemController.ItemController()
                    nxtId = itmCon.nxtid()[0][0]
                    Nid.set(nxtId)
                    tot = 0
                    txtId.focus()
                    return tot
            except:
                None

        #-----------------------------------------------------------------------

        txtSearch = Entry(home, width=12)
        txtSearch.grid(row=0, column=0, padx=10)
        txtSearch.config(font="arial", bg="#CBE2EF")

        scrollbar=Scrollbar(home)
        scrollbar.grid(row=1, column=1, rowspan=8, sticky=N+S)

        lbData = Listbox(home, width=29, height=40, yscrollcommand=scrollbar.set)
        lbData.grid(row=1, column=0, rowspan=22, sticky=N + E)
        lbData.config(bg="#ADC8F6")
        scrollbar.config(command=lbData.yview)

        lblBnr=Label(home, text="Randika Super Centre")
        lblBnr.grid(row=0, column=3, rowspan=2, columnspan=4)
        lblBnr.config(bg="#ADD8E6", font=("Chiller", 42), fg="#200080")

        lblBind = gadget.MyLabel(home, "Bill index : ", 0, 7, None, None, E)
        lblBind.myL()
        lblBdte = gadget.MyLabel(home, "Date : ", 1, 7, None, None, E)
        lblBdte.myL()

        Nid = StringVar()
        txtBind = gadget.MyEntry(home, 0, 8, 12, None, None, None, Nid)
        txtBind.config()

        Date=StringVar()
        date=str(time.localtime()[0])+"."+str(time.localtime()[1])+"."+str(time.localtime()[2])
        Date.set(date)
        lbldte = Label(home, textvariable=Date)
        lbldte.grid(row=1, column=8)
        lbldte.config(font=("Perpetua",17), bg="#ADD8E6")

        line="----------------------------------------"*5
        lblLine = Label(home, text=line)
        lblLine.grid(row=2, column=2, columnspan=7, pady=8)
        lblLine.config(bg="#ADC8F6")

        lblItem = gadget.MyLabel(home, "Item", 3, 2, None, None, W+E)
        lblItem.myL()

        lblNam = gadget.MyLabel(home, "Name", 3, 3, None, None, W + E)
        lblNam.myL()

        lblPrz = gadget.MyLabel(home, "Price", 3, 4, None, None, W + E)
        lblPrz.myL()

        lblDis = gadget.MyLabel(home, "Discount (Rs.)", 3, 5, None, None, W + E)
        lblDis.myL()

        lblQty = gadget.MyLabel(home, "Quantity", 3, 6, None, None, W + E)
        lblQty.myL()

        lblVal = gadget.MyLabel(home, "Value", 3, 7, None, None, W + E)
        lblVal.myL()

        btnAdd = Button(home, text="Add", command=add, font=("Helvetica", 14), width=11)
        btnAdd.grid(row=3, column=8, rowspan=2)
        btnAdd.config(bg="#789AFF")

        varId = StringVar()
        txtId = Entry(home, width=12, textvariable=varId)
        txtId.grid(row=4, column=2)
        txtId.config(font="arial", bg="#CBE2EF")
        txtId.bind('<FocusOut>', dets)

        varName = StringVar()
        varName.set("(no_data)")
        lblName2 = gadget.MyLabel(home, None, 4, 3, 4, None, None, "Rockwell", '#ADD8E6', None, varName)
        lblName2.myL()

        varPrz = StringVar()
        varPrz.set("(no_data)")
        lblPrz2 = gadget.MyLabel(home, None, 4, 4, 4, None, None, "Rockwell", '#ADD8E6', None, varPrz)
        lblPrz2.myL()

        varDis = StringVar()
        varDis.set(0)
        txtDis = Entry(home, width=12, textvariable=varDis)
        txtDis.grid(row=4, column=5)
        txtDis.config(font="arial", bg="#CBE2EF")

        txtQty = Entry(home, width=12)
        txtQty.grid(row=4, column=6)
        txtQty.config(font="arial", bg="#CBE2EF")

        varVal = StringVar()
        varVal.set("(no_data)")
        lblVal2 = gadget.MyLabel(home, None, 4, 7, None, None, None, "Rockwell", '#ADD8E6', None, varVal)
        lblVal2.myL()

        tvData = ttk.Treeview(home, height=20, columns=['id', 'name', 'price', 'qty', 'value'], show='headings')
        tvData.grid(row=5, column=2, columnspan=7, sticky=W + E)

        

        

        btnSave = Button(home, text="Save", command=save, font=("Helvetica", 30))
        btnSave.grid(row=6, column=3, rowspan=3, columnspan=3, sticky=NW + SE)
        btnSave.config(bg="#789AFF")

        lblTot = gadget.MyLabel(home, "Total :", 6, 7, None, None, E)
        lblTot.myL()

        strTotal = StringVar()
        strTotal.set("Rs. 0.0")
        lblTotal = gadget.MyLabel(home, None, 6, 8, 25, None, W, "Rockwell", "#ADC8F6", None, strTotal)
        lblTotal.myL()

        lblTot = gadget.MyLabel(home, "Discount :", 7, 7, None, None, E)
        lblTot.myL()

        txtLDis = gadget.MyEntry(home, 7, 8, 12, None, None, None, None, "arial", "#ADC8F6")
        txtLDis.config()

        varLDis = StringVar()
        varLDis.set(0)
        txtLDis = Entry(home, width=12, textvariable=varLDis)
        txtLDis.grid(row=7, column=8)
        txtLDis.config(font="arial", bg="#ADC8F6")
        txtLDis.bind('<FocusOut>', for_evt)
        txtLDis.bind('<Key>', key_dis)

        lblNet = gadget.MyLabel(home, "Net Amount :", 8, 7, None, None, E)
        lblNet.myL()

        netAmnt = StringVar()
        netAmnt.set("Rs. 0.0")
        lblNetAmn = gadget.MyLabel(home, None, 8, 8, 25, None, W, "Rockwell", "#ADC8F6", None, netAmnt)
        lblNetAmn.myL()

        lbData.bind('<<ListboxSelect>>', clicked)
        home.bind('<Configure>', load)

        txtQty.bind('<Key>', key_evt)
        txtSearch.bind('<Key>', key_evt_src)

        home.mainloop()
