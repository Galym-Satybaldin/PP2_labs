# Retrieving a value using key indexing
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
model_value = car["model"]
print("Car model:", model_value)

# Retrieving a value using the get() method
model_value_get = car.get("model")
print("Car model (using get()):", model_value_get)

# Getting all dictionary keys
keys_list = car.keys()
print("Keys before modification:", keys_list)

# Adding a new key-value pair updates the keys list
car["color"] = "white"
print("Keys after adding 'color':", keys_list)

# Getting all dictionary values
values_list = car.values()
print("Values before modification:", values_list)

# Modifying an existing value updates the values list
car["year"] = 2020
print("Values after updating 'year':", values_list)

# Adding a new key-value pair updates the values list
car["owner"] = "John"
print("Values after adding 'owner':", values_list)

# Getting all dictionary items (key-value pairs as tuples)
items_list = car.items()
print("Items before modification:", items_list)

# Updating a value modifies the items list
car["year"] = 2025
print("Items after updating 'year':", items_list)

# Adding a new item updates the items list
car["country"] = "USA"
print("Items after adding 'country':", items_list)

# Checking if a key exists in the dictionary
if "model" in car:
    print("Yes, 'model' is one of the keys in the dictionary.")
