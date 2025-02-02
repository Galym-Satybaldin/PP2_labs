import math

class Point:
    def __init__(self, x=0, y=0):
        """
        Initializes a new Point object.
        
        Parameters:
            x (float): The x-coordinate (default is 0).
            y (float): The y-coordinate (default is 0).
        """
        self.x = x
        self.y = y

    def show(self):
        """
        Displays the coordinates of the point.
        """
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """
        Moves the point to new coordinates.
        
        Parameters:
            new_x (float): The new x-coordinate.
            new_y (float): The new y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        """
        Computes the Euclidean distance between this point and another point.
        
        Parameters:
            other (Point): Another Point object.
            
        Returns:
            float: The distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Example usage:
p1 = Point(3, 4)
p2 = Point(7, 1)

# Display the coordinates of both points
p1.show()  # Output: (3, 4)
p2.show()  # Output: (7, 1)

# Compute and print the distance between p1 and p2
print("Distance between p1 and p2:", p1.dist(p2))  # Expected output: 5.0

# Move p1 to new coordinates and show the updated point
p1.move(10, 10)
p1.show()  # Output: (10, 10)
