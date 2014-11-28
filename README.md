<h2>The Scenario</h2>

For this project, we'll imagine that you've been hired by a business analyst to build a system that models the bicycle industry. You need to be able to model bicycles, which have a fixed cost to produce, bike shops, which sell bicycles with an added margin on top, and customers, who have different budgets for buying a bicycle.

<h2>Basic Requirements</h2>

<h4>Design Python classes</h4>
You should create classes to represent each of the following parts of our model:
<ul>
<li>Bicycle</li>
<ul>
<li>Have a model name</li>
<li>Have a weight</li>
<li>Have a cost to produce</li>
</ul>
<li>Bike Shops</li>
<ul>
<li>Have a name</li>
<li>Have an inventory of different bicycles</li>
<li>Sell bicycles with a margin over their cost</li>
<li>Can see how much profit they have made from selling bikes</li>
</ul>
<li>Customers</li>
<ul>
<li>Have a name</li>
<li>Have a fund of money to buy a bike</li>
<li>Can buy and own a new bicycle</li>
</ul>
</ul>

<4>Write a script to test your classes</h4>
The script should:
<ul>
<li>Import your classes from a separate file.</li>
<li>Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.</li>
<li>Create three customers. One customer has a budget of $200, the second $500, and the third $1000.</li>
<li>Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.</li>
<li>Print the initial inventory of the bike shop for each bike it carries.</li>
<li>Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.</li>
<li>After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.</li>
</ul>


<h2>Extra Challenge</h2>

If you found completing the basic requirements fairly straightforward then you should try to extend your code to model the bicycles in more detail.

<h4>Alter your classes</h4>
You should add new classes to represent the following bike parts:
<ul>
<li>Wheels</li>
<ul>
<li>Have a model name</li>
<li>Have a weight</li>
<li>Have a cost to produce</li>
<li>There should be a total of three different wheel types</li>
</ul>
<li>Frames</li>
<ul>
<li>Can be made of alminunum, carbon, or steel</li>
<li>Have a weight</li>
<li>Have a cost to produce</li>
</ul>
</ul>

Then you should modify your Bicycle class. The updated class should:
<ul>
<li>Bicycle
<ul>
<li>Be comprised of two wheels of the same type and a frame</li>
<li>Have a weight equal to the sum of the weight of the frame and two wheels</li>
<li>Have a cost to produce equal to the sum of the two wheels' and frame's cost to produce</li>
</ul>
</ul>

You may also need to update your testing script to reflect the changes that you have made here.


<h2>Extension Exercise</h2>

If the extra challenges were not a problem and you're running ahead of schedule then you could try to extend your model even further to add bicycle manufacturers.

<h4>Alter your classes</h4>
You should add one or more classes to represent:
<ul>
<li>Bicycle Manufacturers</li>
<ul>
<li>Have a name</li>
<li>Produce three models of bikes each</li>
<li>Have a percentage over cost which they sell bikes to bike shops at</li>
</ul>
</ul>

Then you should modify your Bicycle class again. The updated class should:
<ul>
<li>Bicycle</li>
<ul>
<li>Have a manufacturer</li>
</ul>
</ul>

<h4>Update your testing script</h4>
The testing script should be modified so that it:
<ul>
<li>Creates two bicycle manufacturers, which both produce three different bicycle models</li>
<li>Makes the bike shops stock their inventory by purchasing bikes from manufacturers</li>
</ul>