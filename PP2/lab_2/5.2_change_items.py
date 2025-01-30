# Modifying a dictionary value using key assignment
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2018
print("Updated year:", car)

# Updating a dictionary using the update() method
car.update({"year": 2020})
print("Updated year using update():", car)
