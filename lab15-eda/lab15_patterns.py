import pandas as pd

df = pd.read_csv("sample.csv")

print("🔹 Missing Values:")
print(df.isnull().sum())

print("\n🔹 Correlation Matrix (numeric only):")
print(df.corr(numeric_only=True))
