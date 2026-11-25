"""
Ex. No. 7 - Data Cleaning and Exploratory Data Analysis Using Pandas

Aim:
    To perform data cleaning, missing value treatment, aggregation and
    exploratory data analysis on a sample real-world-style student dataset
    using Pandas.

The same cleaning steps are applied to two datasets:
    Part 1 - a small dataset created inside the program
    Part 2 - the CSV file students1.csv (kept in this folder)
"""
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()


def clean_and_analyze(df):
    """Clean the DataFrame and print the exploratory data analysis."""
    print("--- Original Dataset ---")
    print(df)

    # Identify missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Missing value treatment: fill numeric gaps with the column mean
    df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
    df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

    # Remove duplicate records
    df = df.drop_duplicates()
    print("\n--- Cleaned Dataset ---")
    print(df)

    # Descriptive statistics
    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    # Aggregation: department-wise average marks
    print("\n--- Department-wise Average Marks ---")
    print(df.groupby("Department")["Mark"].mean().round(2))

    # EDA summary
    print("\n--- EDA Summary ---")
    print("Highest Mark       :", df["Mark"].max())
    print("Lowest Mark        :", df["Mark"].min())
    print("Average Mark       :", round(df["Mark"].mean(), 2))
    print("Average Attendance :", round(df["Attendance"].mean(), 2))


# ---------------- Part 1: dataset created in the program ----------------
print("=============== PART 1 : DATASET CREATED IN CODE ===============\n")
data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82]
}
clean_and_analyze(pd.DataFrame(data))

# ---------------- Part 2: dataset loaded from a CSV file ----------------
print("\n\n=============== PART 2 : DATASET LOADED FROM CSV ===============\n")
filename = BASE / "students1.csv"
clean_and_analyze(pd.read_csv(filename))
