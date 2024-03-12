# NAMES: Mercy Fetzer, Nathan Blickenstaff, Luke Farley, Isabelle Turner, Luke Kehl
# A program that tracks exactly how many hamburgers each customer eats.
# Includes Order, Person, Customer (inherits from Person) classes
# Program includes a dictionary 

import random

class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):  # Added self parameter
        return random.randint(1, 20)
    

class Person():
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):  # Added self parameter
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lsCustomers)
    

class Customer(Person):
    def __init__(self):
        super().__init__()  # Added parentheses after super
        self.order = Order()


dictCustomer = {}
queueCustomers = []

for _ in range(100):  # Use _ as a placeholder for loop variable
    customer = Customer()
    queueCustomers.append(customer)

    if customer.customer_name in dictCustomer:  # Use global dictCustomer
        dictCustomer[customer.customer_name] += customer.order.burger_count
    else:
        dictCustomer[customer.customer_name] = customer.order.burger_count

queueCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)
print()

