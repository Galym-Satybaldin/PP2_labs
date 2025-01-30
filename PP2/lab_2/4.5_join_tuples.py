# Joining two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combined_tuple = tuple1 + tuple2
print("Joined tuple:", combined_tuple)

# Multiplying a tuple
fruits = ("apple", "banana", "cherry")
repeated_fruits = fruits * 2  # Duplicates the tuple elements
print("Multiplied tuple:", repeated_fruits)


# Using count() to find occurrences of a value in a tuple
numbers = (1, 2, 3, 4, 2, 2, 5)
occurrences_of_two = numbers.count(2)
print("Number of times 2 appears in the tuple:", occurrences_of_two)

# Using index() to find the first occurrence of a value in a tuple
fruits = ("apple", "banana", "cherry", "banana", "orange")
first_banana_index = fruits.index("banana")
print("Index of the first 'banana':", first_banana_index)
