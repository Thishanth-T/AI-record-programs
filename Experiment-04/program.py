"""
Ex. No. 4 - Student Record Management Using Lists, Tuples, Dictionaries,
            Files and CSV

Aim:
    To develop a student record management system using Python Lists,
    Tuples, Dictionaries, text file handling and CSV file processing.
"""
import csv
from pathlib import Path

# Files are created next to this script, wherever it is run from
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()

# List of dictionaries: every dictionary is one student record
students = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78},
]

# Tuple example: fixed course details that should not change
course = ("Python", 4)
print("Course Tuple:", course)

# Write the records to a text file
with open(BASE / "students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write the records to a CSV file using the csv module
with open(BASE / "students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read the CSV file back and display the stored records
print("\n--- Records from CSV ---")
with open(BASE / "students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"],
              row["Department"], row["Mark"])
