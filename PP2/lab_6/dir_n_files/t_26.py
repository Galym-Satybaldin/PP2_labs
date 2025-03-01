import string

# Get all uppercase letters A-Z
letters = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create 26 files
for letter in letters:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is file {letter}")
    print(f"Created {filename}")