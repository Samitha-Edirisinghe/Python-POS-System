from tkinter import *
from Report import report
import webbrowser as wb

class ReportViewer():

    def __init__(self, home):

        def genReport():

            rptCon = report.ReportViewer()
            rptCon.reportDaily()
            #rptCon.showPosision()
            messagebox._show("Done", "The Daily Report has been Successfully Generated..!")

        def viewReport():

            wb.open_new(r'C:\Users\Shanuka Dilshan\Desktop\My   Programs\MainProj\Report\Daily_sales_report.pdf')

        home.config(bg="#ADD8E6")

        lblBnr = Label(home, text="Click the button for\ngenerate your sales report")
        lblBnr.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20, sticky=S)
        lblBnr.config(bg="#ADD8E6", font=("Papyrus", 32), fg="#200080")

        btnRView = Button(home, text="Genagrate Daily Sales Report", command=genReport, width=26, height=3, font=("Helvetica", 18))
        btnRView.grid(row=2, column=2, pady=14)
        btnRView.config(bg="#789AFF")

        btnOPN = Button(home, text="View Report", width=10, command=viewReport, font=("Harrington", 10))
        btnOPN.grid(row=3, column=2, pady=80)
        btnOPN.config(bg="#488AC0", fg="#0A0A0A")