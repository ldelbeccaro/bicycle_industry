# Bicycle Industry Project
import sys
import random
try:
    from bike_classes import *
except ImportError:
    print 'Error importing file.'

yellow = Bike('Cruiser', 4, 150)
red = Bike('Mountain', 10, 400)
blue = Bike('Rider', 6, 200)
green = Bike('Fixie', 3, 75)
black = Bike('Intense', 8, 600)
white = Bike('Tricycle', 4, 100)

mikeshop = BikeShop('Mikes Bikes', 0.2)

mikeshop.add_bikes(yellow, 5)
mikeshop.add_bikes(red, 3)
mikeshop.add_bikes(blue, 15)
mikeshop.add_bikes(green, 1)
mikeshop.add_bikes(black, 7)
mikeshop.add_bikes(white, 10)

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
    print person.firstname, 'bought:', person.own, 'Budget remaining:', "{:.2f}".format(person.budget)
mikeshop.printstock()
print mikeshop.name, 'profit:', '{:.2f}'.format(mikeshop.profit())