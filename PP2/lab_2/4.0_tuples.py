# Count the number of items in the tuple
fruits = ("apple", "banana", "cherry")
print("Number of items in the tuple:", len(fruits))

# Creating a tuple with one item requires a comma
# Without the comma, it will be treated as a single value (not a tuple)
one_item_tuple = ("apple",)  # This is a tuple
print("Type of one_item_tuple:", type(one_item_tuple))

# Without the comma, this is a string, not a tuple
not_a_tuple = ("apple")  # Just a string
print("Type of not_a_tuple:", type(not_a_tuple))

# Tuples can store elements of the same or different data types
string_tuple = ("apple", "banana", "cherry")  # Strings
integer_tuple = (1, 5, 7, 9, 3)               # Integers
boolean_tuple = (True, False, False)          # Booleans

# Tuples can also hold mixed data types
mixed_tuple = ("abc", 34, True, 40, "male")
print("A tuple with mixed types:", mixed_tuple)

# Verify that a variable is a tuple using the type() function
my_tuple = ("apple", "banana", "cherry")
print("Type of my_tuple:", type(my_tuple))

# Use the tuple() constructor to create a tuple
# This works for converting other collections like lists into tuples
constructed_tuple = tuple(("apple", "banana", "cherry"))  # Double parentheses
print("Tuple created using tuple():", constructed_tuple)
