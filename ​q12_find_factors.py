# 12 (Finding the factors of an integer) ​q12_find_factors.py
# Write a program that reads an integer and displays all its smallest factors. For example, if the
# input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.


print("Welcome to factor finder!")
number = int(input("Enter a number!"))
factors = []
a = 2
b = 2


while number > b:
    if number % b == 0 & b != number:
        if number % a == 0:
            while number % a == 0:
                factors.append(a)
                number = number / a
        else:
            a = a + 1
    else:
        print("Factors =", factors)
        break

print("Factors =", factors)
