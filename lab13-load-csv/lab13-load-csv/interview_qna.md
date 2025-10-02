# Interview Q&A for Lab 13

**Q1: What is a DataFrame in Pandas?**
A DataFrame is a two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns).

**Q2: How do you check for missing values in a DataFrame?**
By using `df.isnull().sum()` which gives the count of missing values in each column.

**Q3: How do you preview only the first 10 rows of a dataset?**
Use `df.head(10)`.

**Q4: What happens if the CSV file path is incorrect?**
A `FileNotFoundError` will occur.
