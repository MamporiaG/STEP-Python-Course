"""
9-4. Number Served: Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
"""


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant {self.name} has {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open!")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, served_customers):
        self.number_served += served_customers


ita_restaurant = Restaurant("Napoli", "Italian")
ita_restaurant.number_served = 50
print(ita_restaurant.number_served)
ita_restaurant.number_served = 70
print(ita_restaurant.number_served)
ita_restaurant.set_number_served(100)
print(ita_restaurant.number_served)
ita_restaurant.increment_number_served(20)
print(ita_restaurant.number_served)
