# 6 (Conversion from kilograms to pounds) ​q06_kilograms_to_pounds.py
# Write a program that displays the following table (1 kilogram = 2.2 pounds):

input("Kilogram to pound table! (1-100)")
KG = [1]
while max(KG) < 100:
    KG.append(max(KG)+1)
print("Kilograms", "Miles")
for KG[9] in KG:
    print (KG, "       ", float(KG * 2.2)
