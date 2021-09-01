# The number Pie is imported from the library math
import math
radius = float(input("Please enter the radius of the circle: "))

circumference = round(math.pi * radius * 2, 2)
print(f"Circumference: {circumference}")

area = round(math.pi * radius ** 2, 2)
print(f"Area: {area}")


