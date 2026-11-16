
import pandas as pd
from pathlib import Path


# 1. PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# 2. READ INPUT FILE

def load_file():

    file_path = input("\nEnter your file path: ").strip().strip('"')

    path = Path(file_path).expanduser()

    # Resolve relative paths from project folder
    if not path.is_absolute():
        path = BASE_DIR / path

    if not path.exists():
        raise FileNotFoundError("File does not exist!")

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)

    elif path.suffix.lower() == ".xlsx":
        df = pd.read_excel(path)

    else:
        raise ValueError("Only CSV and XLSX files are supported.")

    print("\nFile loaded successfully!")

    return df


# 3. INSPECT DATASET

def inspect_data(df):

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATASET SHAPE ---")
    print(df.shape)

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())


# 4. CLEAN DATASET

def clean_data(df):

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove extra spaces from text values
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Convert empty strings into missing values
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Capture statistics BEFORE cleaning missing values
    original_rows = len(df)
    missing_before = int(df.isnull().sum().sum())
    duplicates_before = int(df.duplicated().sum())

    print("\n--- MISSING VALUES BEFORE CLEANING ---")
    print(df.isnull().sum())

    # Handle missing values
    for column in df.columns:

        if column == "email":
            df[column] = df[column].fillna("Not Provided")

        elif column == "purchase_amount":
            df[column] = df[column].fillna(0)

        elif pd.api.types.is_numeric_dtype(df[column]):

            median_value = df[column].median()

            if pd.notna(median_value):
                df[column] = df[column].fillna(median_value)

            else:
                df[column] = df[column].fillna(0)

        else:
            df[column] = df[column].fillna("Unknown")

    print("\n--- MISSING VALUES AFTER CLEANING ---")
    print(df.isnull().sum())

    # Remove duplicate records
    df = df.drop_duplicates()

    # Capture final statistics
    final_rows = len(df)
    missing_after = int(df.isnull().sum().sum())
    duplicates_after = int(df.duplicated().sum())

    # Create report information
    report = f"""
========== DATA CLEANING REPORT ==========

Original rows: {original_rows}
Final rows: {final_rows}

Duplicates found: {duplicates_before}
Duplicates remaining: {duplicates_after}

Missing values before: {missing_before}
Missing values after: {missing_after}

Rows removed: {original_rows - final_rows}

==========================================
"""

    return df, report


# 5. EXPORT CLEANED DATA

def export_data(df, report):

    # Export CSV
    csv_path = OUTPUT_DIR / "clean_data.csv"
    df.to_csv(csv_path, index=False)

    # Export Excel
    excel_path = OUTPUT_DIR / "clean_data.xlsx"
    df.to_excel(excel_path, index=False)

    # Save cleaning report
    report_path = OUTPUT_DIR / "cleaning_report.txt"
    report_path.write_text(report, encoding="utf-8")

    print("\n--- EXPORT SUCCESSFUL ---")
    print(f"CSV: {csv_path}")
    print(f"Excel: {excel_path}")
    print(f"Report: {report_path}")


# 6. MAIN PROGRAM

def main():

    try:

        # Load dataset
        df = load_file()

        # Inspect original dataset
        inspect_data(df)

        # Clean dataset
        cleaned_df, report = clean_data(df)

        # Display report in terminal
        print(report)

        # Export cleaned files
        export_data(cleaned_df, report)

        print("\nData cleaning process completed successfully!")

    except FileNotFoundError as error:
        print("\nFile Error:", error)

    except ValueError as error:
        print("\nInput Error:", error)

    except pd.errors.EmptyDataError:
        print("\nError: The CSV file is empty.")

    except Exception as error:
        print("\nUnexpected Error:", error)


if __name__ == "__main__":
    main()
