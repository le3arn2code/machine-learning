import pandas as pd
import missingno as msno

# Step 1: Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, None, 40, 35],
    "City": ["New York", "Los Angeles", "Chicago", None, "Miami"],
    "Salary": [50000, 60000, 55000, None, 65000]
}

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("sample.csv", index=False)

# Step 2: Load CSV
df = pd.read_csv("sample.csv")
print("🔹 Loaded DataFrame:")
print(df, "\n")

# Step 3: Inspect missing values
print("🔹 Missing Values Count:")
print(df.isnull().sum(), "\n")

# Step 4: Clean missing values (no inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")

print("🔹 Data after cleaning missing values:")
print(df, "\n")

# Step 5: Optional visualization (skipped in terminal)
try:
    msno.matrix(df)
except Exception as e:
    print("⚠️ Skipping visualization:", e)
