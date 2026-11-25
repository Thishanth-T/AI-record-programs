"""
Ex. No. 13 - AI-Powered Study Assistant Using Python and Generative AI

Aim:
    To develop a Python-based study assistant that retrieves relevant
    learning materials from a CSV dataset and presents study notes and
    quiz information using keyword matching.

Input file : experiment_13_study_materials.csv (6 records)
Note       : matching is based on CSV keyword overlap, not a live
             Generative AI model.
"""
import re
from pathlib import Path

import pandas as pd

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_13_study_materials.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_13_study_materials.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)


def tokenize(text):
    """Convert text into a set of lowercase words (the searchable tokens)."""
    return set(re.findall(r"[a-zA-Z]+", str(text).lower()))


def retrieve_material(query):
    """Return the best matching row and its keyword-overlap score."""
    query_words = tokenize(query)
    scores = []
    for _, row in df.iterrows():
        searchable_text = " ".join([
            row["Topic"], row["Concept"], row["Explanation"], row["Keywords"]
        ])
        material_words = tokenize(searchable_text)
        # Score = fraction of query words found in this study material
        score = len(query_words & material_words) / max(len(query_words), 1)
        scores.append(score)

    best_index = scores.index(max(scores))
    if scores[best_index] == 0:
        return None, 0
    return df.iloc[best_index], scores[best_index]


def study_assistant(query):
    """Display study notes and a quick quiz for the query."""
    material, score = retrieve_material(query)
    if material is None:
        print("No matching material found. Try another concept.")
        return

    print("\n----- PERSONALIZED STUDY NOTES -----")
    print("Topic       :", material["Topic"])
    print("Concept     :", material["Concept"])
    print("Explanation :", material["Explanation"])
    print("Match score :", round(score * 100, 2), "%")

    print("\n----- QUICK QUIZ -----")
    print("Question    :", material["Quiz_Question"])
    print("Difficulty  :", material["Difficulty"])
    print("Answer      :", material["Answer"])


print("Available concepts:", ", ".join(df["Concept"].tolist()))
query = input("\nEnter a topic or concept to study: ")
study_assistant(query)

print("\nStudy assistant session completed.")
print("Note: Matching is based on CSV keyword overlap, not a live Generative AI model.")
