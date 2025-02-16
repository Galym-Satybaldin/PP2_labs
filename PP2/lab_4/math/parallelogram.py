def parallelogram(base, height):
    return base*height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram (base, height)

print (f"Expected Output: {area:.2f}")