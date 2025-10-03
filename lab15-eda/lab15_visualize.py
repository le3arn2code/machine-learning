import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample.csv")

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    # Histogram
    df[col].hist()
    plt.title(f"Distribution of {col}")
    plt.xlabel(col.capitalize())
    plt.ylabel("Frequency")
    plt.savefig(f"lab15_{col}_hist.png")
    plt.clf()

    # Boxplot
    df.boxplot(column=[col])
    plt.title(f"Boxplot of {col}")
    plt.savefig(f"lab15_{col}_boxplot.png")
    plt.clf()
