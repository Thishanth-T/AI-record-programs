# AI-record-programs

Python programs and execution outputs for the **CS6102 – Exploration in Artificial Intelligence** laboratory record (Sep 2026 – Dec 2026), Chennai Institute of Technology (Autonomous).

Each experiment folder contains the complete Python program (`program.py`), the input dataset where one is needed, and an `output.png` captured from a real run of that program.

## Table of Contents

| Ex. No. | Experiment | CO Mapped | Main Libraries |
| :-----: | ---------- | :-------: | -------------- |
| 1  | [Student Marks, Percentage, Grade and Academic Performance](Experiment-01) | CO2 | Python core |
| 2  | [Electricity Billing System Using Conditional Statements and Loops](Experiment-02) | CO2 | Python core |
| 3  | [Menu-Driven Student Information Management](Experiment-03) | CO2 | Python core |
| 4  | [Student Record Management Using Lists, Tuples, Dictionaries, Files and CSV](Experiment-04) | CO2 | `csv` |
| 5  | [IoT Sensor Data Analysis Using NumPy](Experiment-05) | CO2 | NumPy |
| 6  | [Analysis of Student Dataset Using Pandas Series and DataFrame](Experiment-06) | CO2, CO3 | Pandas |
| 7  | [Data Cleaning and Exploratory Data Analysis Using Pandas](Experiment-07) | CO2, CO3 | Pandas |
| 8  | [Data Cleaning, Exploratory Data Analysis and Visualization Using Pandas and Matplotlib](Experiment-08) | CO2, CO3 | Pandas, NumPy, Matplotlib |
| 9  | [Data Visualization Using Matplotlib](Experiment-09) | CO2, CO3 | Pandas, Matplotlib |
| 10 | [Prompt Design and Evaluation Using Generative AI](Experiment-10) | CO2, CO3, CO4 | Pandas |
| 11 | [Role-Based, Zero-Shot, One-Shot and Few-Shot Prompting](Experiment-11) | CO2, CO3, CO4 | Pandas |
| 12 | [AI-Assisted Generation of Technical Content and Python Programs](Experiment-12) | CO2, CO3, CO4, CO5 | Pandas, `pathlib` |
| 13 | [AI-Powered Study Assistant Using Python and Generative AI](Experiment-13) | CO2, CO3, CO4, CO5 | Pandas, `re` |

## Repository Structure

```
AI-record-programs/
├── Experiment-01/ ... Experiment-13/
│   ├── program.py        # Python source code
│   ├── output.png        # Output captured from a real run
│   └── *.csv             # Input dataset (Experiments 7-13)
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3.9 or later
- NumPy, Pandas, Matplotlib

## Setup and Run

```bash
git clone https://github.com/Thishanth-T/AI-record-programs.git
cd AI-record-programs
pip install -r requirements.txt

cd Experiment-01
python program.py
```

Experiments 1, 2, 3 and 13 are interactive and ask for input; the sample values used for the screenshots are shown in each `output.png`. Experiments 7-13 read their CSV file from the experiment folder, so they work from any directory. In Google Colab the programs ask you to upload the CSV if it is not found.

## Notes

- Experiments 8 and 9 also save their charts as PNG files in the experiment folder; `output.png` shows the console output followed by those charts.
- Experiment 4 creates `students.txt` and `students.csv`, and Experiment 12 creates the `generated_technical_content/` folder, when run.
- Experiments 10-13 are rule-based demonstrations, as stated in the lab manual. They do not call a live LLM or any external API.
