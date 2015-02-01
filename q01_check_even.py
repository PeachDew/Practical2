# 1 (Checking whether a number is even) q01_check_even.py
# Write a program that reads an integer and checks whether it is even. 2 sample sessions are as follows:

print("Welcome to even/odd number detector!")
number = input("Enter a number! :D ")
number = int(number)
if number % 2 == 0:
    print("{} is an even number!".format(number))
else:
    print("{} is an odd number!".format(number))
