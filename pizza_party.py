import math


def main():

    print("PIZZA PARTY CALCULATOR")

    number_of_guests = get_number_of_people()

    level_of_appetite = get_appetite_level()

    num_slices = calculate_total_slices(number_of_guests, level_of_appetite)

    slices_per_pizza, pizza_price = get_pizza_size()

    pizzas_needed = calculate_pizzas_needed(num_slices, slices_per_pizza)

    total_cost = calculate_total_cost(pizzas_needed, pizza_price)

    cost_per_person = calculate_cost_per_person(total_cost, number_of_guests)

    leftover_slices = calculate_leftover_slices(
        pizzas_needed, slices_per_pizza, num_slices
    )

    display_results(
        number_of_guests,
        num_slices,
        slices_per_pizza,
        pizzas_needed,
        total_cost,
        cost_per_person,
        leftover_slices,
    )


def get_number_of_people():
    """Prompts the user for the number of people
    Returns an integer
    Must be at least 1
    Keep prompting until valid input received"""
    while True:
        guests = int(input("How many people are coming? "))
        if guests >= 1:
            return guests
        else:
            print("The number of guests shall be at least 1 ")


def get_appetite_level():
    """Displays the three appetite options
    Prompts user to choose 1, 2, or 3
    Returns the number of slices per person (2, 3, or 4)
    Keep prompting until valid choice received"""
    print("How hungry are they?\n")
    print(" 1. Light eaters (2 slices per person)\n")
    print(" 2. Normal appetite (3 slices per person)\n")
    print(" 3. Very hungry (4 slices per person)\n")
    while True:
        slices = int(input("Choose appetite level (1-3): "))
        if slices == 1:
            return 2
        elif slices == 2:
            return 3
        elif slices == 3:
            return 4
        else:
            print("Enter number from 1 to 3 ")


def get_pizza_size():
    """Displays the three pizza size options with prices
    Prompts user to choose 1, 2, or 3
    Returns two values: number of slices per pizza and price per pizza
    Small: 6 slices, $8.99
    Medium: 8 slices, $12.99
    Large: 12 slices, $16.99
    Keep prompting until valid choice received"""
    print("What size pizzas?\n")
    print("1. Small (6 slices, $8.99)\n")
    print("2. Medium (8 slices, $12.99)\n")
    print("3. Large (12 slices, $16.99)\n")
    while True:
        choice = int(input("Choose pizza size (1-3): "))
        if choice < 1 or choice > 3:
            print("Enter a number from 1 to 3")
            continue
        else:
            if choice == 1:
                return 6, 8.99
            elif choice == 2:
                return 8, 12.99
            else:
                return 12, 16.99


def calculate_total_slices(people, slices_per_person):
    """Takes two parameters: number of people and slices per person
    Returns the total number of slices needed
    Formula: people × slices_per_person"""
    return people * slices_per_person


def calculate_pizzas_needed(total_slices, slices_per_pizza):
    num_pizzas = total_slices / slices_per_pizza
    return math.ceil(num_pizzas)


def calculate_total_cost(num_pizzas, price_per_pizza):
    """Takes two parameters: number of pizzas and price per pizza
    Returns the total cost as a float
    Formula: num_pizzas × price_per_pizza"""
    return num_pizzas * price_per_pizza


def calculate_cost_per_person(total_cost, people):
    return total_cost / people


def calculate_leftover_slices(num_pizzas, slices_per_pizza, total_slices):
    """Formula: (num_pizzas × slices_per_pizza) - total_slices"""
    return (num_pizzas * slices_per_pizza) - total_slices


def display_results(
    people,
    total_slices,
    slices_per_pizza,
    num_pizzas,
    total_cost,
    cost_per_person,
    leftover,
):
    """--- PIZZA PARTY PLAN ---
    People: 8
    Total slices needed: 24
    Slices per pizza: 12
    Pizzas to order: 2
    Total cost: $33.98
    Cost per person: $4.25
    Leftover slices: 0"""
    print("--- PIZZA PARTY PLAN ---")
    print(f"People: {people}")
    print(f"Total slices needed: {total_slices}")
    print(f"Slices per pizza: {slices_per_pizza}")
    print(f"Pizzas to order: {num_pizzas}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Cost per person: ${cost_per_person:.2f}")
    print(f"Leftover slices: {leftover}")


if __name__ == "__main__":
    main()
