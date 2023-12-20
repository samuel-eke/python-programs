from oop_lesson import Item
'''
this is an example of inheritance from a class
'''
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        self.broken_phone = broken_phone
        super().__init__(name, price, quantity) #initialization from the super class

phone1 = Phone("phonev10", 500, 2, 2)
phone2 = Phone("phonev20", 423, 4, 1)
