""" class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list
Calculator.add()
dict.values """

""" class User:
    def __init__(self, id, name)
    super(). __init__(id, name) """

class Merchant:
    def  __init__(self, name, products):
    #defines look of class
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant ("Joanna", ['Chicken', 'Pork', 'Beef'])
Joanna.sell('Pork')

Alvin = Merchant ("Alvin", ["Human", "Alvin's Servitude", "Breaks", "Organs"])
Alvin.sell("Human")