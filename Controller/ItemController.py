from Model import Item

class ItemController():

    def __init__(self, itemId=None, name=None, price=None, Clist=None):

        self.ItemId=itemId
        self.name=name
        self.price=price
        self.Clist=Clist

    def save(self):
        itm = Item.Item(self.ItemId,self.name,self.price)
        itm.addItem()

    def update(self):

        itm = Item.Item(self.ItemId, self.name, self.price)
        itm.updItem()

    def delete(self):

        itm = Item.Item(self.ItemId)
        itm.delItem()

    def load(self):

        itm=Item.Item()
        return itm.loadItem()

    def getpr(self):

        itm = Item.Item(self.ItemId)
        return itm.getprz()

    def catlist(self):

        cat = Item.Item(self.Clist)
        return cat.catlist()

    def nxtid(self):

        itm = Item.Item(self.ItemId)
        return itm.nxtid()