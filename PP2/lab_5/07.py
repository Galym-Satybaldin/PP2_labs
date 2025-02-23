def snake_to_camel(string):
    # If string is empty, return empty
    if not string:
        return ''
    
    # Split string by underscores
    words = string.split('_')
    
    # Start with first word as lowercase
    result = words[0].lower()
    
    # Loop through remaining words
    for word in words[1:]:
        # Skip empty parts from extra underscores
        if word:
            # Capitalize first letter, add rest as lowercase
            result += word[0].upper() + word[1:].lower()
    
    return result

# Test cases to try
test_strings = [
    'hello_world',
    'user_id',
    'first_name_last_name',
    'single',
    'snake_case_example',
    '__extra__underscores__',
    '',
    'ALL_CAPS_TEST'
]

# Loop through tests and print results
for test in test_strings:
    result = snake_to_camel(test)
    print(f"Snake: '{test}' -> Camel: '{result}'")