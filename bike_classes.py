# Bicylce Industry Classes

class Wheel(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class High(Wheel):
    intensity = 'high'

class Medium(Wheel):
    intensity = 'medium'

class Low(Wheel):
    intensity = 'low'
    
class Frame(object):
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

class Bike(object):
    Manufacturer = None
    def __init__(self, model, Wheel, Frame):
        makeup = {'wheels': None, 'frame': None}
        self.model = model
        self.Wheel = Wheel
        self.Frame = Frame
        self.makeup['wheels'] = Wheel
        self.makeup['frame'] = Frame
        self.weight = self.makeup['wheels'].weight * 2 + self.makeup['frame'].weight
        self.cost = self.makeup['wheels'].cost * 2 + self.makeup['frame'].cost

class Manufacturer(object):
    models = []
    inventory = {}
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
    def create_bike(self, Bike, number):
        self.models.append(Bike)
        self.inventory[Bike] = number
        Bike.Manufacturer = self
        Bike.cost *= (1 + self.margin)
    
class BikeShop(object):
    inventory = {}
    sold = {}
    prof = 0
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
    def add_bikes(self, Bike, Manufacturer, number):
        if Manufacturer.inventory[Bike] < number:
            print "Cannot add bikes:", Manufacturer, "does not have enough of that model."
        else:
            self.inventory[Bike] = number
            Manufacturer.inventory[Bike] -= 1
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
        self.own = {}
        self.firstname = firstname
        self.budget = budget
    def buy(self, Bike, BikeShop):
        price = Bike.cost * (1 + BikeShop.margin)
        if price > self.budget:
            print 'Cannot buy ' + str(Bike.model) + '! Too expensive.'
        elif BikeShop.inventory[Bike] < 1:
            print 'Cannot buy ' + str(Bike.model) + '! None left in stock.'
        else:
            self.own[Bike.model] = price
            self.budget -= price
            BikeShop.sell_bike(Bike)
        return self.own
