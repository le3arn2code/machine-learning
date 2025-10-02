import pandas as pd

# Load the CSV file
df = pd.read_csv("sample.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
