# 11 (Computing the greatest common divisor) ​q11_find_gcd.py
# A solution to find the greatest common divisor of two integers n1 and n2 is as follows: First
# find d to be the minimum of n1 and n2, then check whether d, d­1, … d­2, 2, or 1 is a divisor
# for both n1 and n2 in this order. The first such common divisor is the greatest common divisor
# for n1 and n2. Write a program to implement this solution.

print("Welcome to the lowest common factor finder!")
number1 = int(input("Key in the first number!"))
number2 = int(input("Key in your second!"))
numberlist = [number1, number2]
lcf = min(numberlist)

while (number1 / lcf) != 1:
    if (number2 / lcf) != 1:
        lcf = lcf - 1
    if lcf == 0:
        print("There is no common factor.")
        break



print("Greatest common factor =", lcf)
