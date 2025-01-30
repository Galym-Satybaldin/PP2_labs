# Creating a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Car dictionary:", car)

# Accessing a dictionary item using its key
print("Car brand:", car["brand"])

# Dictionaries are changeable - modifying a value
car["year"] = 2022
print("Updated year:", car["year"])

# Duplicate keys are not allowed - last value is kept
duplicate_example = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020  # This will overwrite the previous "year" value
}
print("Dictionary with duplicate keys:", duplicate_example)

# Checking dictionary length
print("Number of items in car dictionary:", len(car))

# Dictionaries can store different data types
mixed_data = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print("Mixed data dictionary:", mixed_data)

# Checking the type of a dictionary
print("Type of car dictionary:", type(car))

# Creating a dictionary using the dict() constructor
person = dict(name="John", age=36, country="Norway")
print("Person dictionary:", person)
