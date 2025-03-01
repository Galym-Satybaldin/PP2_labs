import os

# Specify the path to test
path = "my_folder/myfile.txt"

# Check if path exists
if os.path.exists(path):
    print(f"Path '{path}' exists!")
    # Get directory portion
    directory = os.path.dirname(path)
    print(f"Directory: {directory}")
    # Get filename portion
    filename = os.path.basename(path)
    print(f"Filename: {filename}")
else:
    print(f"Path '{path}' does not exist!")