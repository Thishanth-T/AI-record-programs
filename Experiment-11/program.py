"""
Ex. No. 11 - Role-Based, Zero-Shot, One-Shot and Few-Shot Prompting

Aim:
    To demonstrate role-based, zero-shot, one-shot and few-shot prompting
    techniques using CSV-based examples, constructed prompts and
    Python-based demonstration responses.

Input file : experiment_11_prompting_techniques.csv (5 records)
Note       : responses come from simple Python rules, not from a live LLM.
"""
from pathlib import Path

import pandas as pd

# Locate the CSV next to this script (in Google Colab, upload it if missing)
BASE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
CSV_FILE = BASE / "experiment_11_prompting_techniques.csv"
if not CSV_FILE.exists():
    try:
        from google.colab import files  # only available inside Google Colab
        files.upload()
        CSV_FILE = Path("experiment_11_prompting_techniques.csv")
    except ImportError:
        raise SystemExit(f"Input file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)

# Keyword sets used by the demonstration sentiment classifier
positive_words = {"quick", "perfectly", "excellent", "helpful", "love", "early", "great"}
negative_words = {"poor", "dull", "stopped", "broken", "slow", "unavailable"}


def sentiment_demo(sentence):
    """Classify a sentence as Positive / Negative / Neutral using keyword counts."""
    words = set(sentence.lower().replace(".", "").replace(",", "").split())
    score = len(words & positive_words) - len(words & negative_words)
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"


def construct_prompt(row):
    """Build the prompt text according to the prompting technique."""
    role = row["Role"]
    task = row["Task"]
    text = row["Input_Text"]
    technique = row["Technique"]

    if technique == "Zero-Shot":      # no example is given
        return f"You are a {role}. {task}: {text}"
    if technique == "One-Shot":       # exactly one example is given
        return (f"You are a {role}. {task}. Example: "
                f"{row['Example_Input']} -> {row['Example_Output']}. New input: {text}")
    if technique == "Few-Shot":       # several examples are given
        return (f"You are a {role}. {task}. Examples: "
                "Excellent service -> Positive; Poor quality -> Negative. "
                f"New input: {text}")
    return f"Act as a {role}. {task}: {text}"   # role-based prompt


print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")
for _, row in df.iterrows():
    prompt = construct_prompt(row)

    # Predefined Python rules generate the demonstration response
    if "sentiment" in row["Task"].lower():
        response = sentiment_demo(row["Input_Text"])
    elif "priority" in row["Task"].lower():
        response = "High" if "unavailable" in row["Input_Text"].lower() else "Low"
    else:
        response = "Suggested rewrite: Please share the project file at your earliest convenience."

    print(f"\nID: {row['Example_ID']} | Technique: {row['Technique']}")
    print("Constructed prompt:", prompt)
    print("Python demonstration response:", response)

print("\nDemonstration completed. Responses use predefined Python rules, not a live LLM.")
