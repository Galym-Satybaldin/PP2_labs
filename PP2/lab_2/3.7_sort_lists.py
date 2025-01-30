# Sorting a list of strings alphabetically
fruit_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_list.sort()
print(fruit_list)

# Sorting a list of numbers in descending order
number_list = [100, 50, 65, 82, 23]
number_list.sort(reverse=True)
print(number_list)

# Sorting a list of strings in reverse alphabetical order
reverse_fruit_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
reverse_fruit_list.sort(reverse=True)
print(reverse_fruit_list)

# Sorting a list of numbers based on their distance from 50
def distance_from_fifty(n):
    return abs(n - 50)

custom_sort_list = [100, 50, 65, 82, 23]
custom_sort_list.sort(key=distance_from_fifty)
print(custom_sort_list)

# Sorting a list of strings alphabetically, case-insensitive
mixed_case_list = ["banana", "Orange", "Kiwi", "cherry"]
mixed_case_list.sort(key=str.lower)
print(mixed_case_list)

# Sorting a list of strings alphabetically with default case-sensitive sort
case_sensitive_list = ["banana", "Orange", "Kiwi", "cherry"]
case_sensitive_list.sort()
print(case_sensitive_list)

# Reversing the order of a list of strings
reversed_list = ["banana", "Orange", "Kiwi", "cherry"]
reversed_list.reverse()
print(reversed_list)
