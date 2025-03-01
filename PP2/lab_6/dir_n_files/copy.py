# Create a sample source file
with open("source.txt", "w") as file:
    file.write("This is the source file content.\nHello!")

# Copy contents to destination file
with open("source.txt", "r") as source:
    with open("destination.txt", "w") as destination:
        destination.write(source.read())

# Verify by reading destination file
with open("destination.txt", "r") as file:
    print("Contents of destination.txt:")
    print(file.read())