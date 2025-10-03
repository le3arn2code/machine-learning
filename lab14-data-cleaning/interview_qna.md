# Interview Q&A - Lab 14

**Q1. How do you handle missing numerical data in Pandas?**  
A: Use `df['column'].fillna(df['column'].mean())` for replacing with mean, or median if distribution is skewed.

**Q2. How do you handle missing categorical data?**  
A: Replace with mode or placeholder like `"Unknown"`.

**Q3. What is the difference between `dropna()` and `fillna()`?**  
A: `dropna()` removes rows/columns with missing values, while `fillna()` replaces them with a value.

**Q4. Why avoid using `inplace=True` in Pandas?**  
A: Future versions of Pandas will deprecate it. It's safer to reassign values directly.
