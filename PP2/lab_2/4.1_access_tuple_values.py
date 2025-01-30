# Accessing tuple elements by index
fruits = ("apple", "banana", "cherry")
print("Second item:", fruits[1])  # Indexing starts from 0

# Accessing the last item using negative indexing
print("Last item:", fruits[-1])  # -1 refers to the last element

# Accessing a range of items (from index 2 to 4, index 5 is excluded)
extended_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Subset (index 2 to 4):", extended_fruits[2:5])

# Accessing elements from the start up to a specific index (index 4 is excluded)
print("First four items:", extended_fruits[:4])

# Accessing elements from a specific index to the end
print("From index 2 to the end:", extended_fruits[2:])

# Using negative indexing to get a range (from -4 to -1, -1 is excluded)
print("Negative index range (-4 to -1):", extended_fruits[-4:-1])

# Checking if an item exists in a tuple
if "apple" in fruits:
    print("Yes, 'apple' is in the tuple.")
