
# Python Data Cleaner

A Python-based data cleaning tool that helps clean messy CSV and Excel datasets using Pandas.

## Features

- Read CSV and Excel files
- Standardize column names
- Remove extra spaces
- Handle missing values
- Remove duplicate records
- Export cleaned data into CSV and Excel formats

## Technologies Used

- Python
- Pandas
- OpenPyXL

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Navigate to the project folder:

```bash
cd python-data-cleaner
```

Run:

```bash
python cleaner.py
```

Enter the CSV or Excel file path when prompted.

## Project Structure

```text
python-data-cleaner/
├── data/
├── output/
├── cleaner.py
├── requirements.txt
└── README.md
```

## Author

Kunal Rana

## Additional Features

- Supports CSV and XLSX input files.
- Validates file paths and file formats.
- Handles missing values and duplicate records.
- Generates a cleaning report.
- Exports cleaned data into CSV and Excel formats.
- Uses modular functions for better code organization.
- Includes error handling for common input problems.

## Output Files

After execution, the output folder contains:

- clean_data.csv
- clean_data.xlsx
- cleaning_report.txt