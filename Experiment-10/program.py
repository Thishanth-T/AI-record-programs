"""
Ex. No. 10 - Prompt Design and Evaluation Using Generative AI

Aim:
    To design and evaluate effective prompts using a structured CSV dataset
    and Python-based criteria such as role, context, task clarity,
    constraints and output format.

Input file : experiment_10_prompt_evaluation.csv (5 records)
Note       : this is a rule-based prompt-quality checklist, not an LLM call.
"""
from pathlib import Path

import pandas as pd

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_10_prompt_evaluation.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_10_prompt_evaluation.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)


def evaluate_prompt(prompt):
    """Score a prompt (0-5) by checking five prompt-design features."""
    text = prompt.lower()
    features = {
        "Role": any(word in text for word in ["act as", "you are"]),
        "Context": any(word in text for word in
                       ["student", "manager", "college", "project", "report"]),
        "Clear task": any(word in text for word in
                          ["explain", "draft", "review", "summarize", "compare"]),
        "Constraints": any(word in text for word in
                           ["words", "bullet", "under", "three", "five"]),
        "Output format": any(word in text for word in
                             ["table", "subject", "bullet points", "example"])
    }
    return sum(features.values()), features


print("----- PROMPT DESIGN AND EVALUATION -----")
for _, row in df.iterrows():
    weak_score, _ = evaluate_prompt(row["Weak_Prompt"])
    improved_score, features = evaluate_prompt(row["Improved_Prompt"])

    print(f"\nPrompt ID: {row['Prompt_ID']} | Task: {row['Task']}")
    print(f"Weak prompt score     : {weak_score}/5")
    print(f"Improved prompt score : {improved_score}/5")
    print("Satisfied features    :", ", ".join(k for k, v in features.items() if v))
    print("Evaluation            :", "Improved" if improved_score > weak_score else "Needs review")

# Score every prompt and compare the averages
df["Weak_Score"] = df["Weak_Prompt"].apply(lambda x: evaluate_prompt(x)[0])
df["Improved_Score"] = df["Improved_Prompt"].apply(lambda x: evaluate_prompt(x)[0])

print("\n----- OVERALL SUMMARY -----")
print("Average weak prompt score    :", round(df["Weak_Score"].mean(), 2))
print("Average improved prompt score:", round(df["Improved_Score"].mean(), 2))
print("\nEvaluation completed. This is a rule-based prompt-quality checklist, not an LLM evaluation.")
