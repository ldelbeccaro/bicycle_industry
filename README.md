The Scenario

For this project, we'll imagine that you've been hired by a business analyst to build a system that models the bicycle industry. You need to be able to model bicycles, which have a fixed cost to produce, bike shops, which sell bicycles with an added margin on top, and customers, who have different budgets for buying a bicycle.

Basic Requirements

Design Python classes
You should create classes to represent each of the following parts of our model:

Bicycle
- Have a model name
- Have a weight
- Have a cost to produce
Bike Shops
- Have a name
- Have an inventory of different bicycles
- Sell bicycles with a margin over their cost
- Can see how much profit they have made from selling bikes
Customers
- Have a name
- Have a fund of money to buy a bike
- Can buy and own a new bicycle

Write a script to test your classes
The script should:

- Import your classes from a separate file.
- Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
- Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
- Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
- Print the initial inventory of the bike shop for each bike it carries.
- Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
- After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.



Extra Challenge

If you found completing the basic requirements fairly straightforward then you should try to extend your code to model the bicycles in more detail.

Alter your classes
You should add new classes to represent the following bike parts:

Wheels
- Have a model name
- Have a weight
- Have a cost to produce
- There should be a total of three different wheel types
Frames
- Can be made of aluminunum, carbon, or steel
- Have a weight
- Have a cost to produce

Then you should modify your Bicycle class. The updated class should:

Bicycle
- Be comprised of two wheels of the same type and a frame
- Have a weight equal to the sum of the weight of the frame and two wheels
- Have a cost to produce equal to the sum of the two wheels' and frame's cost to produce
- You may also need to update your testing script to reflect the changes that you have made here.

Extension Exercise

If the extra challenges were not a problem and you're running ahead of schedule then you could try to extend your model even further to add bicycle manufacturers.

Alter your classes
You should add one or more classes to represent:

Bicycle Manufacturers
- Have a name
- Produce three models of bikes each
- Have a percentage over cost which they sell bikes to bike shops at

Then you should modify your Bicycle class again. The updated class should:

Bicycle
- Have a manufacturer

Update your testing script
The testing script should be modified so that it:

- Creates two bicycle manufacturers, which both produce three different bicycle models
- Makes the bike shops stock their inventory by purchasing bikes from manufacturers