from Model import Catogary

class CatogaryController():

    def __init__(self, Cid=None, Discription=None):

        self.Cid=Cid
        self.Discription=Discription

    def save(self):
        cat = Catogary.Catogary(self.Cid,self.Discription)
        cat.addCat()

    def delete(self):
        cat = Catogary.Catogary(self.Cid)
        cat.delCat()