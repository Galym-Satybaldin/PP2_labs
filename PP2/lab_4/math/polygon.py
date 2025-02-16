import math

def regular_polygon_area(n, s):
    if n < 3:
        return "A polygon must have at least 3 sides."
    
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

# Example usage:
num_sides = int(input("Input number of sides: "))
side_length = int(input("Input the length of a side: "))

area = regular_polygon_area(num_sides, side_length)
print(f"The area of the polygon is: {area:.2f}")
