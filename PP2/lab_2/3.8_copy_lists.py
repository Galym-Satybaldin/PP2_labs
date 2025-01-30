# Method 1: Using the slice operator
fruit_list = ["apple", "banana", "cherry"]
copied_list_slice = fruit_list[:]
print(copied_list_slice)

# Method 2: Using the list() function
original_list = ["apple", "banana", "cherry"]
copied_list_function = list(original_list)
print(copied_list_function)

# Method 3: Using the copy() method
main_list = ["apple", "banana", "cherry"]
copied_list_copy_method = main_list.copy()
print(copied_list_copy_method)
