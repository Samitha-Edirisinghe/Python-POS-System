from Controller import ReportController
from reportlab.lib import colors
import time

class myDraw():

    def __init__(self, c):
        self.c = c

    def showPosision(self, c):

        c = self.c

        c.drawString(0, 0, "0")
        c.drawString(0, 100, "100")
        c.drawString(0, 200, "200")
        c.drawString(0, 300, "300")
        c.drawString(0, 400, "400")
        c.drawString(0, 500, "500")
        c.drawString(0, 600, "600")
        c.drawString(0, 700, "700")
        c.drawString(0, 800, "800")

        c.drawString(0, 830, "0")
        c.drawString(100, 830, "100")
        c.drawString(200, 830, "200")
        c.drawString(300, 830, "300")
        c.drawString(400, 830, "400")
        c.drawString(500, 830, "500")
        c.drawString(600, 830, "600")

        c.save()

        return c

    #---------------------------------------------------

    def reportDaily(self, c):

        c = self.c

        rptCon = ReportController.ReportController()
        data = rptCon.daily_rep()

        bill_index = []
        total = []
        discount = []
        net = []
        for i in data:
            bill_index.append(i[0])
            total.append(i[1])
            discount.append(i[2])
            net.append(i[3])

        c.setFillColor(colors.darkblue)
        c.rect(6, 5, 584, 832, fill=0)

        c.drawString(410, 820, "Shanuwa's Shopping Centre")

        c.drawImage('logo.jpg', 439, 733, width=100, height=84) #the_logo

        c.drawString(401, 725, "..All your needs from one place..")


        c.drawString(20, 780, "No.62/2,")
        c.drawString(20, 760, "Station Road,")
        c.drawString(20, 740, "Gampola.")
        date = str(time.localtime()[0]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[2])
        c.drawString(20, 720, date)
        c.drawString(20, 690, "😏 Summery Of Daily Sales Report")

        #lines------------------------
        c.line(20,689,204,689)
        c.line(85, 645, 502, 645)
        #-----------------------------

        c.drawString(108, 653, "Invoice#")
        coun = 0
        yaxe = 628
        while (coun < len(bill_index)):
            c.drawString(125, yaxe, str(bill_index[coun]))
            yaxe = yaxe - 17
            coun += 1

        c.drawString(214, 653, "Total")
        coun = 0
        l_tot = 0
        yaxe = 628
        while (coun < len(total)):
            c.drawString(211, yaxe, str(total[coun]))
            l_tot += total[coun]
            yaxe = yaxe - 17
            coun += 1

        c.drawString(315, 653, "Discount")
        coun = 0
        l_dis = 0
        yaxe = 628
        while (coun < len(discount)):
            c.drawString(326, yaxe, str(discount[coun]))
            l_dis += discount[coun]
            yaxe = yaxe - 17
            coun += 1

        c.drawString(420, 653, "Net Amount")
        coun = 0
        yaxe = 628
        while (coun < len(net)):
            c.drawString(432, yaxe, str(net[coun]))
            yaxe = yaxe - 17
            coun += 1

        #rectangles-------------------------------
        ynew = yaxe+3
        c.rect(85, ynew, 418, 672-ynew, fill=0)
        c.rect(178, yaxe-43, 215, 672-ynew+46, fill=0)
        #-----------------------------------------
        c.line(284, 672, 284, ynew)

        c.drawString(200, yaxe - 18, "Total of total           =    ")
        c.drawString(328, yaxe - 18, str(l_tot))

        c.drawString(200, yaxe - 33, "Total of discount     =    ")
        c.drawString(328, yaxe - 33, str(l_dis))

        c.save()

        return c
