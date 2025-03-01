# Program to multiply all numbers in a list using built-in function
numbers = [2, 3, 4, 5]  # Our sample list

# Using reduce() from functools and lambda to multiply all numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

print(f"List: {numbers}")
print(f"Product of all numbers: {product}")  # Output: 120 (2*3*4*5)