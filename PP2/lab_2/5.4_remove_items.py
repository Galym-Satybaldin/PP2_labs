# Removing an item using pop() - removes a specific key
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
print("Dictionary after pop('model'):", car)

# Removing the last inserted item using popitem()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.popitem()
print("Dictionary after popitem():", car)

# Removing an item using the del keyword
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car["model"]
print("Dictionary after del car['model']:", car)

# Deleting the entire dictionary using del (this will raise an error if accessed afterward)
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car
# print(car)  # Uncommenting this will cause an error as the dictionary no longer exists

# Clearing all items in a dictionary using clear()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
print("Dictionary after clear():", car)  # Outputs an empty dictionary {}
