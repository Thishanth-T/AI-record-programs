"""
Ex. No. 9 - Data Visualization Using Matplotlib

Aim:
    To develop a Python program using Pandas and Matplotlib to analyze
    retail sales data from a CSV file and represent the information
    through different graphical visualizations such as line charts,
    bar charts, pie charts and scatter plots.

Input file : experiment_9_retail_sales.csv (24 records, 6 columns)
Charts     : saved as PNG files in this folder and also displayed.
"""
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Show all columns (wrapped) instead of truncating wide tables
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 80)

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_9_retail_sales.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_9_retail_sales.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

# Read the dataset and convert the Date column to datetime
df = pd.read_csv(CSV_FILE)
df["Date"] = pd.to_datetime(df["Date"])

# Revenue of every transaction = units sold x unit price
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("----- RETAIL SALES DATASET -----")
print(df.head())

# Total sales analysis
print("\nTotal Units Sold:", df["Units_Sold"].sum())
print("Total Revenue: Rs.", df["Revenue"].sum())

# Monthly revenue
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
print("\n----- MONTHLY REVENUE -----")
print(monthly_sales)

# Category-wise revenue
category_sales = df.groupby("Category")["Revenue"].sum()
print("\n----- CATEGORY-WISE REVENUE -----")
print(category_sales)

# Region-wise revenue
region_sales = df.groupby("Region")["Revenue"].sum()
print("\n----- REGION-WISE REVENUE -----")
print(region_sales)

# Visualization 1: Monthly revenue line chart
plt.figure(figsize=(9, 5))
monthly_sales.index = monthly_sales.index.astype(str)
plt.plot(monthly_sales.index, monthly_sales.values,
         marker="o", linewidth=2, label="Monthly Revenue")
plt.title("Monthly Retail Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(BASE / "chart_1_monthly_revenue.png", dpi=120)
plt.show()

# Visualization 2: Category-wise bar chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("Category-wise Revenue Comparison")
plt.xlabel("Product Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(BASE / "chart_2_category_revenue.png", dpi=120)
plt.show()

# Visualization 3: Region-wise pie chart
plt.figure(figsize=(7, 7))
plt.pie(region_sales, labels=region_sales.index,
        autopct="%1.1f%%", startangle=90)
plt.title("Region-wise Revenue Distribution")
plt.tight_layout()
plt.savefig(BASE / "chart_3_region_revenue.png", dpi=120)
plt.show()

# Visualization 4: Units sold vs revenue scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Units_Sold"], df["Revenue"], color="red", marker="o")
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(BASE / "chart_4_units_vs_revenue.png", dpi=120)
plt.show()

print("\nData Visualization Completed Successfully!")
