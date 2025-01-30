# Method 1: Concatenating two lists with the + operator
letters_list = ["a", "b", "c"]
numbers_list = [1, 2, 3]

combined_list_plus = letters_list + numbers_list
print("Combined list using + operator:", combined_list_plus)

# Method 2: Extending a list with another list
letters_list = ["a", "b", "c"]
numbers_list = [1, 2, 3]

letters_list.extend(numbers_list)
print("List after using extend():", letters_list)

# Method 3: Appending items from one list to another in a loop
letters_list = ["a", "b", "c"]
numbers_list = [1, 2, 3]

for num in numbers_list:
    letters_list.append(num)

print("List after appending items in a loop:", letters_list)
