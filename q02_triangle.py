#  (Validating triangles and computing perimeter) q02_triangle.py
# Write a program that reads three edges for a triangle and determines whether the input is valid.
# The input is valid if the sum of any two edges is greater than the third edge. The program will
# compute the perimeter of the triangle if the input is valid. Otherwise, display that the input is invalid.

print("Welcome to triangle perimeter calculator!")
side1 = int(input("Key in the first length of the triangle! :D"))
side2 = int(input("Key in the second length of the triangle! :D"))
side3 = int(input("Key in the third length of the triangle! :D"))
side = [side1, side2, side3, (side1 + side2), (side2 + side3), (side3 + side1)]
if min(side) == ((side1 + side2) or (side2 + side3) or (side3 + side1)):
    print("Invalid Triangle!")
else:
    print("Perimeter of the triangle is {}! :D".format(side1+side2+side3))
