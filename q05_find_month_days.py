# 5 (Finding the number of days in a month) ​q05_find_month_days.py
# Write a program that prompts the user to enter the month and year, and displays the number
# of days in the month. For example, if the user entered month 2 and year 2000, the program
# should display that February 2000 has 29 days. If the user entered month 3 and year 2005,
# the program should display that March 2005 has 31 days.

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

print("Welcome to days in month calculator!")
year = int(input("Enter year"))
month = int(input("Enter month (1-12)"))
if month == 2:
    if year % 400 == 0:
        print("There are 29 days!")
    elif year % 4 == 0 and year % 100 != 0:
        print("There are 29 days!")
    else:
        print("There are 28 days!")
if month in month_31:
    print("There are 31 days!")
if month in month_30:
    print("There are 30 days!")
