import math

print(" Squares, Square roots, Cubes, and Cube Roots")

# Take number from user
num = int(input("Enter a number: "))

# Square
print("Square of", num, "=", num ** 2)

# Square root
print("Square root of", num, "=", math.sqrt(num))

# Cube
print("Cube of", num, "=", num ** 3)

# Cube root
print("Cube root of", num, "=", num ** (1/3))