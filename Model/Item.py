import DB

class Item():

    def __init__(self,ID=None, Name=None, Price=None, bill_index=None, date=None, discount=None, discountx=None, quantity=None, treeall=None):

        self.myDB=DB.DBCon()
        self.ID=ID
        self.Name=Name
        self.Price=Price
        self.bill_index = bill_index
        self.date = date
        self.discount = discount
        self.discountx = discountx
        self.quantity = quantity
        self.treeall = treeall

    def addItem(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="INSERT INTO Item (ID, Name, Price) VALUES (%s, %s, %s)"
        values=(self.ID, self.Name, self.Price)

        cur.execute(sql, values)

        myCon.commit()


    def updItem(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="UPDATE item SET Name=%s, Price=%s WHERE ID=%s"
        values=(self.Name, self.Price, self.ID)

        cur.execute(sql, values)

        myCon.commit()

    def delItem(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="DELETE FROM item WHERE ID={}".format(self.ID)

        cur.execute(sql)

        myCon.commit()

    def getprz(self):

        myCon = self.myDB.conn()
        cur = myCon.cursor()

        sql = "SELECT Price FROM item WHERE ID={}".format(self.ID)
        cur.execute(sql)
        Pr = cur.fetchall()[0][0]

        return Pr

    def loadItem(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="SELECT ID, Name FROM item"
        cur.execute(sql)
        data=cur.fetchall()

        return data

    def catlist(self):

        myCon = self.myDB.conn()
        cur = myCon.cursor()

        sql="SELECT Cid, Discription FROM catogary"
        cur.execute(sql)
        Clist = cur.fetchall()

        return Clist

    def getitem(self):

        myCon = self.myDB.conn()
        cur = myCon.cursor()

        sql = "SELECT id, name, price FROM item WHERE id={}".format(self.ID)
        cur.execute(sql)
        detail = cur.fetchall()
        return detail

    def nxtid(self):

        myCon = self.myDB.conn()
        cur = myCon.cursor()

        sql = "SELECT MAX(bill_index)+1 FROM sale_sum"
        cur.execute(sql)
        Nxtid = cur.fetchall()

        return Nxtid

    def saveSum(self):
        myCon = self.myDB.conn()
        cur = myCon.cursor()

        sql1 = "INSERT INTO sale_sum (bill_index,date,discount) VALUES ('{}','{}','{}')".format(self.bill_index,self.date,self.discount)
        cur.execute(sql1)

        for det in self.treeall:
            sql2 = "INSERT INTO sale_det (id, price, bill_index, discount, quentity) VALUES (%s,%s,%s,%s,%s)"
            values = (det[0], det[2], self.bill_index, self.discount, det[3])
            cur.execute(sql2, values)

        myCon.commit()
