"""
Ex. No. 1 - Student Marks, Percentage, Grade and Academic Performance

Aim:
    To develop a Python application that accepts student marks, calculates
    total marks, percentage and grade, and displays the academic performance
    using variables, operators, expressions and input/output operations.
"""

# Read the student's name and the number of subjects
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

# Read the mark of every subject and add it to the running total
total = 0
for i in range(1, n + 1):
    mark = float(input(f"Enter mark for Subject {i}: "))
    total += mark

# Percentage (each subject is assumed to be out of 100)
percentage = total / n

# Decide grade and performance status using conditional statements
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs Improvement"

# Display the result
print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Performance :", performance)
