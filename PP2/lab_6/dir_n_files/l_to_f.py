# Sample list
my_list = ["Apple", "Banana", "Orange"]

# Write list to file
with open("fruits.txt", "w") as file:
    for item in my_list:
        file.write(f"{item}\n")  # Write each item on a new line

# Verify by reading back
with open("fruits.txt", "r") as file:
    print("Contents of fruits.txt:")
    print(file.read())