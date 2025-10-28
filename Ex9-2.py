""" "9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant {self.name} has {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open!")


ita_restaurant = Restaurant("Napoli", "Italian")
mex_restaurant = Restaurant("Taco Bell", "Mexican")
esp_restaurant = Restaurant("Madird", "Spanish")


ita_restaurant.describe_restaurant()
mex_restaurant.describe_restaurant()
esp_restaurant.describe_restaurant()
