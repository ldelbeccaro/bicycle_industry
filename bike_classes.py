# Bicylce Industry Classes
class Bike(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
class BikeShop(object):
    inventory = {}
    sold = {}
    prof = 0
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
    def add_bikes(self, Bike, number):
        self.inventory[Bike] = number
        return self.inventory
    def sell_bike(self, Bike):
        price = Bike.cost * (1 + self.margin)
        self.inventory[Bike] -= 1
        self.sold[Bike] = price
        return self.sold
    def printstock(self):
        print 'Current inventory for ' + str(self.name) + ':'
        for bike in self.inventory:
            print bike.model, self.inventory[bike]
    def profit(self):
        for Bike in self.sold:
            self.prof += (self.sold[Bike] - Bike.cost)
        return self.prof
class Customer(object):
    def __init__(self, firstname, budget):
        self.firstname = firstname
        self.budget = budget
        self.own = {}
    def buy(self, Bike, BikeShop):
        price = Bike.cost * (1 + BikeShop.margin)
        if price > self.budget:
            print 'Cannot buy ' + str(Bike.model) + '! Too expensive.'
        elif BikeShop.inventory[Bike] < 1:
            print 'Cannot buy ' + str(Bike.model) + '! None left in stock.'
        else:
            self.own[Bike.model] = '{:.2f}'.format(price)
            self.budget -= price
            BikeShop.sell_bike(Bike)
        return self.own
    