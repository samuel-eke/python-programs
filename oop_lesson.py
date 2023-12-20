import csv

class Item:
    #to create a class-level attribute, you declare it within here
    pay_rate = 0.8
    all_list = []
    def __init__(self, name:str, price:float, quantity=0 ): 
        '''
        the above is a constructor
        #the zero allows that particular attribute to be parsed in optionally
        #declaring a type for an argument, makes it explicitly clear that it can only accept a certain data type
        #Run validations for arguments
        assert price >= 0, f"Price {price} is not greater than zero" #this is an assert-error message to display incase of an error
        assert quantity >= 0
        #the attributes within this module are called instance attributes
        '''
        Item.all_list.append(self) #this statement adds all instances of Item class created, to the list above

        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self): #this can be said to be a method
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod #this line, treats the below method as a class-level method
    def from_csv(cls):
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)
    @staticmethod
    def is_integer(num):
        pass

    def __repr__(self): #this magic method helps us to represent strings in a readable format
        return f"{self.name, self.price, self.quantity}"

Item.from_csv()
print (Item.all_list)
#print(Item.all_list)

#print (Item.__dict__) #this gives us all attributes at the different levels, for this one, its the class level
#print (item1.__dict__) #gives us all attributes at the instance level


