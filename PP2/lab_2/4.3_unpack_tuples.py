# Packing a tuple (assigning multiple values into a tuple)
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple (extracting values into variables)
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Unpacking with an asterisk (*) to collect remaining values into a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # "red" will be a list containing the remaining elements

print(green)
print(yellow)
print(red)  # Outputs ['cherry', 'strawberry', 'raspberry']

# Using an asterisk in a non-final position
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits  # "tropic" collects all middle values

print(green)
print(tropic)  # Outputs ['mango', 'papaya', 'pineapple']
print(red)
