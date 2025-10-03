import pandas as pd

df = pd.read_csv("sample.csv")

print("🔹 First 5 rows of the dataset:")
print(df.head())

print("\n🔹 Dataset Info:")
df.info()

print("\n🔹 Summary Statistics:")
print(df.describe())
