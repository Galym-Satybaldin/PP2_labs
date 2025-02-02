class Shape:
    def area(self):
        # The default area for a generic shape is 0.
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        # Calculate the area of the square (side * side) and print it.
        print(self.length * self.length)

# Example usage:
# Create an instance of Shape and call its area method.
shape = Shape()
shape.area()  # Output: 0

# Create an instance of Square with a side length of 4 and call its area method.
square = Square(4)
square.area()  # Output: 16
