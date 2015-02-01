# 7 (Conversion from miles to kilometres) ​q07_miles_to_kilometres.py
# Write a program that displays the following two tables side­by­side (note that 1 mile is 1.609
# kilometres):

print("Welcome to Miles and Kilometres conversion table!")
print("")
import time
time.sleep(1)
print("Miles", "Kilometres", "Kilometres", "Miles")
for x in range(1,11):
    kilo = x*5
    print("{0:<6}{1:<11}{2:<11}{3:<.5}".format(x, x*1.609, kilo+15, (kilo+15)/1.609 ))
