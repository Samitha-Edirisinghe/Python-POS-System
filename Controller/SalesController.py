from Model import Item


class SalesController():

    def __init__(self, itemId=None, bill_index=None, date=None, discount=None, price=None, discountx=None, quantity=None, treeall=None):
        self.itemId = itemId
        self.bill_index = bill_index
        self.date = date
        self.discount = discount
        self.price = price
        self.discountx = discountx
        self.quantity = quantity
        self.treeall = treeall

    def addItem(self):
        sale = Item.Item(self.itemId)
        data=sale.getitem()

        if data==[]:
            return 0
        else:
            return data

    def saveSum(self):

        itm = Item.Item(None, None, None, self.bill_index, self.date, self.discount, None, self.quantity, self.treeall)
        itm.saveSum()