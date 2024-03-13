# NAMES: Mercy Fetzer, Nathan Blickenstaff, Luke Farley, Isabelle Turner, Luke Kehl
# A program that tracks exactly how many hamburgers each customer eats.
# Includes Order, Person, Customer (inherits from Person) classes
# Program includes a dictionary 

import random

#class for order
#initializes amount of burgers in the order through obtaining a random number between 1 and 20
class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):  # Added self parameter
        return random.randint(1, 20)
    
#class for person
#initializes the customer name variable through obtaining a random name from a predetermined list
class Person():
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):  # Added self parameter
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lsCustomers)
    
#class for customer
#inherits from person, initializes with an order class
class Customer(Person):
    def __init__(self):
        super().__init__()  # Added parentheses after super
        self.order = Order()

#initializes a dictionary and a list for storing customers
dictCustomer = {}
queueCustomers = []

#for loop that stores the amount of burgers that each of the customer has ordered
#customers are from the predetermined list found within person.randomname
for _ in range(100):  # Use _ as a placeholder for loop variable
    customer = Customer()
    queueCustomers.append(customer)

    if customer.customer_name in dictCustomer:  # Use global dictCustomer
        dictCustomer[customer.customer_name] += customer.order.burger_count
    else:
        dictCustomer[customer.customer_name] = customer.order.burger_count

#sorts list by most number of burgers ordered
queueCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)
print()

#for loop for printing each customer and the total amount of burgers ordered.
for customer in queueCustomers:

    print(customer[0].ljust(19) + "   " + str(customer[1]) + "\n")
