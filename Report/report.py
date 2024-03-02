from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import reportGadget

c = canvas.Canvas("Report/Daily_sales_report.pdf", pagesize=A4)

class ReportViewer():

        def showPosision(self):

            global c
            rptGad = reportGadget.myDraw(c)
            posision = rptGad.showPosision(c)
            return posision

        def reportDaily(self):

            global c
            rptGad = reportGadget.myDraw(c)
            daily_report = rptGad.reportDaily(c)
            return daily_report
