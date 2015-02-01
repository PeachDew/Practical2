# 3 (Determining grade) q03_determine_grade.py
# Write a program that prompts the user to enter a score between 0 and 100 inclusive. The grading system is as follows:
# A: 70 - 100
# B: 60 - 69
# C: 55 - 59
# D: 50 - 54
# E: 45 - 49
# S: 35 - 44
# U: 0 - 35

A = [70]
while max(A) < 100:
    A.append(max(A)+1)
B = [60]
while max(B) < 69:
    B.append(max(B)+1)
C = [55]
while max(C) < 59:
    C.append(max(C)+1)
D = [50]
while max(D) < 54:
    D.append(max(D)+1)
E = [45]
while max(E) < 49:
    E.append(max(E)+1)
S = [35]
while max(S) < 44:
    S.append(max(S)+1)
U = [0]
while max(U) < 35:
    U.append(max(U)+1)

print("DHS grading system")
valid_x = False
while not valid_x:
    grade = int(input("Key in your score. ( /100)"))
    if grade > 100 or grade < 0:
        print("Score is out of range")
    else:
        if grade in A:
            print("Your grade: A")
        if grade in B:
            print("Your grade: B")
        if grade in C:
            print("Your grade: C")
        if grade in D:
            print("Your grade: D")
        if grade in E:
            print("Your grade: E")
        if grade in S:
            print("Your grade: S")
        if grade in U:
            print("Your grade: U")
        valid_x = True
