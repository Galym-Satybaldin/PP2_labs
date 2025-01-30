# Demonstrating useful Python list methods

# 1. append(): Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("After append:", fruits)

# 2. extend(): Adds elements of another list to the current list
vegetables = ["carrot", "potato", "spinach"]
fruits.extend(vegetables)
print("After extend:", fruits)

# 3. sort(): Sorts the list in ascending order
numbers = [42, 7, 13, 99, 21]
numbers.sort()
print("After sort (ascending):", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("After sort (descending):", numbers)
