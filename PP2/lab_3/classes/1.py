class StringManipulator:
    def __init__(self):
        # Initialize the string attribute to an empty string.
        self.s = ""
    
    def getString(self):
        # Get a string from console input and store it in the instance attribute.
        self.s = input("Enter a string: ")
    
    def printString(self):
        # Print the stored string in upper case.
        print(self.s.upper())

# Example usage:
obj = StringManipulator()  # Create an instance of the class.
obj.getString()            # Call the method to get a string from the user.
obj.printString()          # Call the method to print the string in upper case.
