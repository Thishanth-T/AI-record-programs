"""
Ex. No. 12 - AI-Assisted Generation of Technical Content and Python Programs

Aim:
    To develop a Python application that generates structured technical
    explanations and reusable Python program templates from task
    specifications stored in a CSV file.

Input file : experiment_12_technical_generation.csv (5 records)
Output     : generated_technical_content/ (one .py and one _notes.txt per task)
Note       : template-based generation - no external LLM is called.
"""
from pathlib import Path

import pandas as pd

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_12_technical_generation.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_12_technical_generation.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE, encoding="utf-8")

# Predefined Python program templates, one for each technical topic
templates = {
"CSV Data Analysis": '''import pandas as pd
def column_average(filename, column):
    data = pd.read_csv(filename)
    if column not in data.columns:
        raise ValueError("Column not found")
    values = pd.to_numeric(data[column], errors="coerce").dropna()
    if values.empty:
        raise ValueError("No numeric values available")
    return round(values.mean(), 2)
''',
"Temperature Conversion": '''def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be numeric")
    return round((celsius * 9 / 5) + 32, 2)
''',
"Password Validation": '''def check_password(password):
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special character": any(not c.isalnum() for c in password)
    }
    for rule, passed in checks.items():
        print(rule, ":", "Pass" if passed else "Fail")
    return all(checks.values())
''',
"List Statistics": '''def list_statistics(values):
    if not values:
        raise ValueError("List cannot be empty")
    return {"minimum": min(values), "maximum": max(values),
            "range": max(values) - min(values)}
''',
"Text Analysis": '''import string
def analyze_text(text):
    cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    return {"total_words": len(words), "unique_words": len(set(words))}
'''
}

# Folder where the generated explanations and programs are saved
output_dir = BASE / "generated_technical_content"
output_dir.mkdir(exist_ok=True)

print("----- TECHNICAL CONTENT AND PYTHON PROGRAM GENERATION -----")
for _, row in df.iterrows():
    topic = row["Topic"]
    code = templates[topic]

    # Build the structured explanation for this task
    explanation = (
        f"Topic: {topic}\nAudience: {row['Audience']}\n"
        f"Task: {row['Task_Description']}\n"
        f"Requirements: {row['Requirements']}\n"
        "Approach: validate inputs, process data and present a clear result."
    )

    # Save the program and its notes as separate files
    file_stem = row["Task_ID"].lower()
    (output_dir / f"{file_stem}.py").write_text(code, encoding="utf-8")
    (output_dir / f"{file_stem}_notes.txt").write_text(explanation, encoding="utf-8")

    print(f"\nTask ID: {row['Task_ID']} | Topic: {topic}")
    print(explanation)
    print("Saved:", f"{file_stem}.py", "and", f"{file_stem}_notes.txt")

print("\nTotal generated files:", len(list(output_dir.iterdir())))
print("Template-based generation completed. No external LLM is called.")
