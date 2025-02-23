def camel_to_snake(string):
    # New string to build with underscores
    result = ''
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If character is uppercase and not first, add underscore
        if string[i].isupper() and i > 0:
            result += '_' + string[i].lower()
        # Otherwise, just add it as lowercase
        else:
            result += string[i].lower()
    
    return result

# Test cases to try
test_strings = [
    'HelloWorld',
    'userId',
    'FirstNameLastName',
    'XMLParser',
    'single',
    'OneTwoThree',
    '',
    'ABC'
]

# Loop through tests and print results
for test in test_strings:
    result = camel_to_snake(test)
    print(f"Camel: '{test}' -> Snake: '{result}'")