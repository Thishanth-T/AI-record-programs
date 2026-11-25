"""
Ex. No. 6 - Analysis of Student Dataset Using Pandas Series and DataFrame

Aim:
    To create and manipulate Pandas Series and DataFrames for analyzing
    a student dataset.
"""
import pandas as pd

# A Series is a one-dimensional labelled array (marks indexed by letters)
marks = pd.Series([85, 91, 78, 88, 95],
                  index=["A", "B", "C", "D", "E"])
print("--- Pandas Series ---")
print(marks)

# A DataFrame is a two-dimensional table built from a dictionary of columns
data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": [85, 91, 78, 88, 95]
}
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)

# Average mark of the class
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

# Filter high-performing students (boolean indexing)
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
