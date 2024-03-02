from Controller import CatogaryController
from tkinter import *
from tkinter import messagebox
import gadget

class CatogaryForm():

        def __init__(self, home):

                #home.title("Catogary Form")
                home.config(bg="#ADD8E6")

                #--------------------------------------------------
                #Defs
                #--------------------------------------------------

                def save():

                        cd = txtcd.get()
                        ds = txtds.get()

                        catCon = CatogaryController.CatogaryController(cd, ds)
                        catCon.save()

                def delete():

                        cd = txtcd.get()

                        catCon = CatogaryController.CatogaryController(cd)
                        catCon.delete()

                #--------------------------------------------------------------------------
                #User Intrface
                #--------------------------------------------------------------------------

                lblcd = gadget.MyLabel(home, "Code", 0, 0, 10)
                lblcd.myL()

                lbldot1 = gadget.MyLabel(home, ":", 0, 1, None, None, None, "Broadway")
                lbldot1.myL()

                txtcd = gadget.MyEntry(home, 0, 2, 15, 10, 10, W, None, None)
                txtcd.config()

                lblds=gadget.MyLabel(home, "Discription", 1, 0, 10)
                lblds.myL()

                lbldot2 = gadget.MyLabel(home, ":", 1, 1, None, None, None, "Broadway")
                lbldot2.myL()

                txtds = gadget.MyEntry(home, 1, 2, 15, 10, 10, W, None, None)
                txtds.config()

                btnsv = gadget.MyButton(home, "Save", save, 2, 0, 7, 12, 12, None)
                btnsv.myB()

                btndl = gadget.MyButton(home, "Delete", delete, 2, 2, 7, 12, 12, None)
                btndl.myB()

                #-----------------------------------------------------------------------

                home.mainloop()
