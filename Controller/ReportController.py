from Model import Report
from Report import report

total = 0
dis = 0

class ReportController():

    def __init__(self, bill_index=None, total=None, discount=None, netamount=None, date=None):
        self.bill_index = bill_index
        self.total = total
        self.discount = discount
        self.netamount = netamount
        self.date = date

    def daily_rep(self):
        mrpt = Report.Report(None, None, None, None, self.date)
        daily = mrpt.daily_rep()
        return daily

    def showPosision(self):
        rptViw = report.ReportViewer()
        rptViw.showPosision()
