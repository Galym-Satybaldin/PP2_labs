# Create a sample file first (for testing)
with open("sample.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\nLine 4")

# Count lines
with open("sample.txt", "r") as file:
    line_count = sum(1 for line in file)  # Count each line
print(f"Number of lines in sample.txt: {line_count}")  # Output: 4