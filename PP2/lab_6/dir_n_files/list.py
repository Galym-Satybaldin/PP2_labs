import os

# Specify the path (current directory in this case)
path = "."

# List only directories
print("Directories:")
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
for dir_name in dirs:
    print(dir_name)

# List only files
print("\nFiles:")
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
for file_name in files:
    print(file_name)

# List all (directories and files)
print("\nAll items:")
all_items = os.listdir(path)
for item in all_items:
    print(item)