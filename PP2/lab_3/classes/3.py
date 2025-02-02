class Shape:
    def area(self):
        # Default area for a generic shape is 0.
        print(0)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Compute and print the area of the rectangle.
        print(self.length * self.width)

# Example usage:
rect = Rectangle(5, 3)  # Create a Rectangle with length 5 and width 3.
rect.area()             # Output: 15
