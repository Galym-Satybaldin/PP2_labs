# Sample dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Print all keys
for key in car:
    print(key)

# Print all values
for key in car:
    print(car[key])

# Print values using values() method
for value in car.values():
    print(value)

# Print keys using keys() method
for key in car.keys():
    print(key)

# Print both keys and values using items() method
for key, value in car.items():
    print(key, value)

# Copy using copy() method
copy1 = car.copy()
print(copy1)

# Copy using dict() function
copy2 = dict(car)
print(copy2)