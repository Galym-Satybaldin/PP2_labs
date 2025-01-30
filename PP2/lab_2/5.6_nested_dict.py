# Creating a nested dictionary
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}

# Alternative way: Creating separate dictionaries and combining them
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily_alt = {"child1": child1, "child2": child2, "child3": child3}

# Accessing an item in a nested dictionary
print("Child2's name:", myfamily["child2"]["name"])

# Looping through a nested dictionary
for key, value in myfamily.items():
    print(key)  # Outer dictionary keys (child1, child2, child3)
    for sub_key, sub_value in value.items():
        print(sub_key + ":", sub_value)  # Inner dictionary keys and values
