import math

def trapezoid_area(height, base1, base2) :

    return ((base1 + base2) * height / 2)


height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))


area = trapezoid_area(height, base1, base2)

print ("Expected Output: ", area)