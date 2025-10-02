# Interview Q&A - Lab 12: Pandas Series and DataFrames

**Q1: What is a Pandas Series?**
A1: A one-dimensional labeled array that can hold any data type. It is similar to a column in Excel.

**Q2: What is a DataFrame in Pandas?**
A2: A two-dimensional data structure with labeled rows and columns, similar to an Excel sheet or SQL table.

**Q3: How do you create a DataFrame from a dictionary?**
A3: Use `pd.DataFrame(dictionary)` where keys are column names and values are lists.

**Q4: What is the difference between loc[] and iloc[]?**
A4: `loc[]` accesses rows/columns by labels, while `iloc[]` accesses by integer position.

**Q5: How can you add a new column to a DataFrame?**
A5: Assign a list/Series to a new column name, e.g., `df['Country'] = ['USA','USA','USA']`.

**Q6: How do you modify a specific value in a DataFrame?**
A6: Use `.at[row_index, 'column_name'] = new_value`.

**Q7: What are common use cases of Pandas in data science?**
A7: Data cleaning, transformation, analysis, and integration with libraries like NumPy, Matplotlib, and Scikit-learn.

**Q8: What is the significance of indices in Pandas?**
A8: Indices uniquely identify rows and make data selection and manipulation easier.

**Q9: How can you check data types of DataFrame columns?**
A9: Use `df.dtypes`.

**Q10: How do you export a DataFrame to a CSV file?**
A10: Use `df.to_csv('filename.csv', index=False)`.
