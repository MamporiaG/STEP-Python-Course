# # Assignment 1

# """
# Write a Python function that takes a list of numbers as a parameter and returns the sum of the numbers.
# The function should take the following list as a parameter: [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# """


# def sum_of_list(*numbers):
#     total = 0
#     for nums in numbers:
#         total += nums
#     return total


# numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# print(sum_of_list(*numbers))

# Assignment 2

"""
Using recursion, write a Python function that will take one parameter number and return the sum of its digits.
Example: If the function receives the number 12345, it should return 15, because 1 + 2 + 3 + 4 + 5 = 15.

"""


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


# print(sum_of_digits(12345))
print(12345 % 10)

