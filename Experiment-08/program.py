"""
Ex. No. 8 - Data Cleaning, Exploratory Data Analysis and Visualization
            Using Pandas and Matplotlib

Aim:
    To develop a Python program using Pandas and Matplotlib to load a
    student performance dataset from a CSV file, identify and handle
    missing values, remove duplicate records, perform exploratory data
    analysis, calculate statistical measures and visualize the cleaned data.

Input file : experiment_8_student_performance.csv (22 records, 6 columns)
Charts     : saved as PNG files in this folder and also displayed.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Show all columns (wrapped) instead of truncating wide tables
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 80)

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_8_student_performance.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_8_student_performance.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)

print("----- ORIGINAL DATASET -----")
print(df.head())
print("\nDataset Shape:", df.shape)

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Handle missing numerical values using median imputation
num_cols = df.select_dtypes(include=np.number).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Handle missing categorical (text) values using mode imputation
cat_cols = df.select_dtypes(exclude=np.number).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicate records
df = df.drop_duplicates()

# Calculate the average score of every student
df["Average_Score"] = df[["Assignment_Score", "Exam_Score"]].mean(axis=1)

# Classify academic performance using score ranges
df["Performance"] = pd.cut(
    df["Average_Score"],
    bins=[-1, 50, 70, 85, 100],
    labels=["Needs Improvement", "Average", "Good", "Excellent"]
)

print("\n----- CLEANED DATASET -----")
print(df.head(10))
print("\nCleaned Dataset Shape:", df.shape)

# Statistical analysis
print("\n----- STATISTICAL SUMMARY -----")
print(df.describe().round(2))

# Department-wise comparison
dept_analysis = df.groupby("Department")["Exam_Score"].mean()
print("\n----- DEPARTMENT-WISE AVERAGE -----")
print(dept_analysis.round(2))

# Performance distribution
print("\n----- PERFORMANCE DISTRIBUTION -----")
print(df["Performance"].value_counts())

# Visualization 1: Department-wise average exam score
plt.figure(figsize=(8, 5))
dept_analysis.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Department-wise Average Exam Score")
plt.xlabel("Department")
plt.ylabel("Average Exam Score")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(BASE / "chart_1_department_average.png", dpi=120)
plt.show()

# Visualization 2: Student performance distribution
plt.figure(figsize=(8, 5))
df["Performance"].value_counts().plot(kind="bar", color="orange", edgecolor="black")
plt.title("Student Performance Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(BASE / "chart_2_performance_distribution.png", dpi=120)
plt.show()

print("\nData Cleaning and EDA Completed Successfully!")
