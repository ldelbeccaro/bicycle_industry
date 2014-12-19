# Bicycle Industry Project
import sys
import random
try:
    from bike_classes import *
except ImportError:
    print 'Error importing file.'

wheel1 = Low('cool', 2, 40)
wheel2 = Medium('brisk', 3, 60)
wheel3 = High('frigid', 4, 150)
wheel4 = Low('chilly', 2, 25)

frame1 = Frame('warm', 3, 70)
frame2 = Frame('scorching', 5, 100)
frame3 = Frame('hot', 2, 80)
frame4 = Frame('lukewarm', 1, 25)
frame5 = Frame('humid', 4, 300)

yellow = Bike('Cruiser', wheel1, frame1)
red = Bike('Mountain', wheel3, frame2)
blue = Bike('Rider', wheel2, frame3)
green = Bike('Fixie', wheel4, frame4)
black = Bike('Intense', wheel3, frame5)
white = Bike('Tricycle', wheel4, frame4)
white.cost = white.makeup['wheels'].cost * 3 + white.makeup['frame'].cost

maker1 = Manufacturer('Bike Emporium', 0.1)
maker2 = Manufacturer('Biker Kingdom', 0.05)

maker1.create_bike(yellow, 40)
maker1.create_bike(red, 40)
maker1.create_bike(blue, 40)
maker2.create_bike(green, 50)
maker2.create_bike(black, 50)
maker2.create_bike(white, 50)

mikeshop = BikeShop('Mikes Bikes', 0.2)
mikeshop.add_bikes(yellow, maker1, 5)
mikeshop.add_bikes(red, maker1, 3)
mikeshop.add_bikes(blue, maker1, 15)
mikeshop.add_bikes(green, maker2, 1)
mikeshop.add_bikes(black, maker2, 7)
mikeshop.add_bikes(white, maker2, 10)

Laura = Customer('Laura', 200)
Michael = Customer('Michael', 500)
Hannah = Customer('Hannah', 1000)
mikecustomers = [Laura, Michael, Hannah]

for person in mikecustomers:
    person.affordable = []
    print person.firstname, 'can buy:'
    for bike in mikeshop.inventory:
        price = bike.cost * (1 + mikeshop.margin)
        if price <= person.budget:
            print bike.model, '{:.2f}'.format(price)
            person.affordable.append(bike)
mikeshop.printstock()
for person in mikecustomers:
    person.buy(random.choice(person.affordable), mikeshop)
    print person.firstname, 'bought:', person.own, 'Budget remaining:', '{:.2f}'.format(person.budget)
mikeshop.printstock()
print mikeshop.name, 'profit:', '{:.2f}'.format(mikeshop.profit())