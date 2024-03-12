# NAMES: Mercy Fetzer, Nathan Blickenstaff, Luke Farley, Isabelle Turner, Luke Kehl
# A program that tracks exactly how many hamburgers each customer eats.
# Includes Order, Person, Customer (inherits from Person) classes
# Program includes a dictionary 

import random

class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(): # outputs a random integer from 1 - 20
        return random.randint(1, 20)
      
    
class Person():
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(): # outputs a random name for  the lsCustomers list
        lsCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lsCustomers)
    

class Customer(Person):
    def __init__(self):
        super.__init__()
        self.order = Order()


customer = {}

queueCustomers = []

queueCustomers.append(Customer)

for iCount in range(0, len(queueCustomers)):
    print(queueCustomers[iCount])

for iCount in range(1, len(queueCustomers) + 1):
    queueCustomers.pop(0)

    for iCount in range(0, len(queueCustomers)):
        print(queueCustomers[iCount])
