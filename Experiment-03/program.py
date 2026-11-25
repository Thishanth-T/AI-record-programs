"""
Ex. No. 3 - Menu-Driven Student Information Management

Aim:
    To implement a menu-driven Python application using functions and
    modular programming concepts to manage basic student information.
"""

# Dictionary that stores all student records: {roll_no: {"Name": ..., "Department": ...}}
students = {}


def add_student():
    """Read the details of a student and store them in the dictionary."""
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")


def view_students():
    """Display all stored student records."""
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, data in students.items():
        print("Roll No:", roll,
              "| Name:", data["Name"],
              "| Department:", data["Department"])


def search_student():
    """Search a student using the roll number."""
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def delete_student():
    """Delete a student using the roll number."""
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Show the menu repeatedly until the user selects Exit
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
