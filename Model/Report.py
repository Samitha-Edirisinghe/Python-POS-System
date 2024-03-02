import DB
import time

#---------------------------------------------------

class Report():

    def __init__(self, bill_index=None, total=None, discount=None, netamount=None, date=None):
        self.myDB = DB.DBCon()
        self.bill_index = bill_index
        self.total = total
        self.discount = discount
        self.netamount = netamount
        self.date = date

    #---------------------------------------------------

    def daily_rep(self):
        myCon = self.myDB.conn()
        cur = myCon.cursor()

        dateN = str(time.localtime()[0]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[2])

        sql = "SELECT sale_sum.bill_index,sum(sale_det.price*sale_det.quentity) AS tot,\
                sale_sum.discount, sum(sale_det.price*sale_det.quentity)-sale_sum.discount AS net\
                FROM sale_sum LEFT JOIN sale_det ON sale_sum.bill_index=sale_det.bill_index\
                 WHERE sale_sum.date = '{}'\
                 GROUP BY sale_det.bill_index".format(dateN)

        cur.execute(sql)
        daily_data = cur.fetchall()

        return daily_data