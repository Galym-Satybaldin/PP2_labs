def get_permutations(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in get_permutations(remaining):
            result.append(char + perm)
    
    return result

# Get input from the user.
user_input = input("Enter a string: ")

# Get all permutations of the user input.
permutations = get_permutations(user_input)

# Print all permutations.
print("Permutations of the string are:")
for perm in permutations:
    print(perm)



