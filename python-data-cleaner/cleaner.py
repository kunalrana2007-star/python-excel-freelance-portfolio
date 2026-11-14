import pandas as pd
import os

file_path = input("enter yout file path: ")

if file_path.lower().endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.lower().endswith(".xlsx"):
    df = pd.read_excel(file_path)

else:
    print("Unsupported file path")
    exit()
print("\n file loaded successfully")


# 1. Display first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# 2. Check rows and columns
print("\n--- DATASET SHAPE ---")
print(df.shape)

# 3. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# 5. Check data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 6. Standardize the column name
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n--- CLEANED COLUMN NAMES ---")
print(df.columns.tolist())


# 7. Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

print("\n--- SPACES REMOVED ---")
print(df.head())

# 8. Check missing values
print("\n--- MISSING VALUES BEFORE CLEANING ---")
print(df.isnull().sum())

# 9. Fill missing age with median age
df["age"] = df["age"].fillna(df["age"].median())

# 10. Fill missing email with a placeholder
df["email"] = df["email"].fillna("Not Provided")

# 11. Fill missing purchase amount with 0
df["purchase_amount"] = df["purchase_amount"].fillna(0)

print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df.isnull().sum())


# 12. Count duplicates before cleaning
print("\nDuplicates before cleaning:", df.duplicated().sum())

# 13. Remove duplicate records
df = df.drop_duplicates()

# 14. Count duplicates after cleaning
print("Duplicates after cleaning:", df.duplicated().sum())

# 15. Display updated dataset size
print("Final dataset shape:", df.shape)


os.makedirs("output",exist_ok=True)
df.to_csv("output/clean_data.csv",index=False)
df.to_excel("output/clean_data.xlsx",index=False)

print("\n--- EXPORT SUCCESSFUL ---")
print("Cleaned CSV: output/cleaned_data.csv")
print("Cleaned Excel: output/cleaned_data.xlsx")