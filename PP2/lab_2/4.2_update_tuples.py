# Tuples are immutable (unchangeable), but we can work around this by converting to a list.

# 1. Changing a tuple value by converting it to a list
fruits = ("apple", "banana", "cherry")
temp_list = list(fruits)  # Convert tuple to list
temp_list[1] = "kiwi"  # Modify the value
fruits = tuple(temp_list)  # Convert back to tuple
print("Tuple after modification:", fruits)

# 2. Adding an item to a tuple (Workaround: Convert to list, add, and convert back)
fruits = ("apple", "banana", "cherry")
temp_list = list(fruits)
temp_list.append("orange")  # Adding a new element
fruits = tuple(temp_list)
print("Tuple after adding an item:", fruits)

# 3. Adding items using tuple concatenation
fruits = ("apple", "banana", "cherry")
new_fruit = ("orange",)  # Tuple with a single item (comma is required)
fruits += new_fruit  # Concatenating tuples
print("Tuple after tuple concatenation:", fruits)

# 4. Removing an item from a tuple (Workaround: Convert to list, remove, and convert back)
fruits = ("apple", "banana", "cherry")
temp_list = list(fruits)
temp_list.remove("apple")  # Removing an item
fruits = tuple(temp_list)
print("Tuple after removing an item:", fruits)

# 5. Deleting a tuple completely
fruits = ("apple", "banana", "cherry")
del fruits  # The tuple is now deleted

# This will raise an error because the tuple no longer exists
# print(fruits)  
