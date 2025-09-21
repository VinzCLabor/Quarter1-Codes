import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * (r ** 2)
area_rounded = round(area, 2)
print(f"The area of a circle with radius {r} is: {area_rounded}")
