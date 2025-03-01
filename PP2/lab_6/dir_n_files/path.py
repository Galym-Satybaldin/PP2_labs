import os

# Specify the path to check
path = "myfile.txt"

# Check existence
exists = os.path.exists(path)
print(f"Path exists: {exists}")

# Check readability
readable = os.access(path, os.R_OK)
print(f"Readable: {readable}")

# Check writability
writable = os.access(path, os.W_OK)
print(f"Writable: {writable}")

# Check executability
executable = os.access(path, os.X_OK)
print(f"Executable: {executable}")