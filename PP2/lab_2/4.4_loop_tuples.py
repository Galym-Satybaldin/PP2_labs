# Loop through a tuple using a for loop
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Loop through a tuple using index numbers
fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
    print(fruits[i])

# Loop through a tuple using a while loop
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1  # Increment the index
