# 1. fromkeys(): Create a dictionary with default values
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print("Dictionary created with fromkeys():", default_dict)

# 2. setdefault(): Get a value, or insert if key doesn’t exist
person = {"name": "Alice", "age": 25}
city = person.setdefault("city", "New York")  # Adds key if missing
print("Updated dictionary after setdefault():", person)

# 3. popitem(): Remove and return the last inserted item
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
last_item = car.popitem()
print("Dictionary after popitem():", car)
print("Removed item:", last_item)
