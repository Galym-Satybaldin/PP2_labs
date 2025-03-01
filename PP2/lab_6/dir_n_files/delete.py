import os

# Specify the path to delete
path = "file_to_delete.txt"

# Create a sample file for testing
with open(path, "w") as file:
    file.write("This file will be deleted.")

# Check existence and access
if os.path.exists(path):
    print(f"Path '{path}' exists!")
    if os.access(path, os.W_OK):  # Check if writable (can delete)
        os.remove(path)
        print(f"File '{path}' deleted successfully!")
    else:
        print(f"No write access to delete '{path}'!")
else:
    print(f"Path '{path}' does not exist!")