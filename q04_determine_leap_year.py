# 4 (Determining leap year) ​q04_determine_leap_year.py
# Write a program that prompts the user to enter a year and determines whether it is a leap
# year. A year is a leap year if it is divisible by 4 but not 100, or is divisible by 400.

print("Welcome to the leap year detector!")
year = int(input("Enter year"))
if year % 400 == 0:
    print("{} is a leap year!".format(year))
elif year % 4 == 0 and year % 100 != 0:
    print("{} is a leap year!".format(year))
else:
    print("{} is not a leap year!".format(year))
