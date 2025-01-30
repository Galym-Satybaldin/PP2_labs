# Adding a new key-value pair using direct assignment
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
print("Dictionary after adding 'color':", car)

# Adding a new key-value pair using the update() method
car.update({"owner": "John"})
print("Dictionary after adding 'owner' using update():", car)
