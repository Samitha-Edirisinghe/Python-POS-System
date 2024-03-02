import DB

class Catogary():

    def __init__(self, Cid=None, Discription=None):

        self.myDB=DB.DBCon()
        self.Cid=Cid
        self.Discription=Discription

    def addCat(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="INSERT INTO catogary (Cid, Discription) VALUES (%s, %s)"
        values=(self.Cid, self.Discription)

        cur.execute(sql, values)

        myCon.commit()

    def delCat(self):

        myCon=self.myDB.conn()
        cur=myCon.cursor()

        sql="DELETE FROM catogary WHERE Cid='{}'".format(self.Cid)

        cur.execute(sql)

        myCon.commit()