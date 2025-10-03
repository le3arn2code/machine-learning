# Troubleshooting Guide for Lab 15

1. **ModuleNotFoundError: No module named 'pandas'**
   - Fix: Install Pandas using `pip install pandas --break-system-packages`.

2. **ModuleNotFoundError: No module named 'matplotlib'**
   - Fix: Install Matplotlib using `pip install matplotlib --break-system-packages`.

3. **ModuleNotFoundError: No module named 'seaborn'**
   - Fix: Install Seaborn using `pip install seaborn --break-system-packages`.

4. **Correlation Matrix Error (ValueError: could not convert string to float)**
   - Fix: Ensure correlation is computed only on numeric columns using:
     ```python
     df.corr(numeric_only=True)
     ```
