# 8 (Finding the two highest scores) ​q08_top2_scores.py
# Write a program that prompts the user to enter the number of students and each student's
# name and score, and finally displays the student with the highest score and the student with
# the second­highest score.

print("Welcome to highest scorer detector!")
students = []
scores = []
students_no = int(input("How many students are there?"))

x = 1
while x <= students_no:
    x = x + 1
    name = input("Key in the name of a student!")
    students.append(name)

print("In the same way you entered the students,")
x = 1
while x <= students_no:
    valid_x = False
    while not valid_x:
        marks = input("Key in the marks of a student!")
        if not marks.isdigit():
            print("Key in a number!")
        else:
            x = x + 1
            scores.append(marks)
            valid_x = True


print("Highest scorer:", students[int(scores.index(max(scores)))])
print("He/She scored ", max(scores))

students.remove(students[scores.index(max(scores))])
scores.remove(max(scores))

print("Second highest scorer:", students[scores.index(max(scores))])
print("He/She scored ", max(scores))
