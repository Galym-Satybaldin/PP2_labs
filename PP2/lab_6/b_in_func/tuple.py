# Program to check if all tuple elements are True
def all_true(tup):
    return all(tup)  # Built-in all() returns True if all elements are True

# Test cases
tuple1 = (True, True, 1, "hello")  # All considered True in Python
tuple2 = (True, False, 1, 0)      # Contains False values

print(f"Tuple 1: {tuple1}")
print(f"All elements true? {all_true(tuple1)}")  # True
print(f"Tuple 2: {tuple2}")
print(f"All elements true? {all_true(tuple2)}")  # False