# Troubleshooting - Lab 12

1. **ModuleNotFoundError: No module named 'pandas'**
   - Install Pandas using: `pip3 install pandas --break-system-packages`

2. **ModuleNotFoundError: No module named 'numpy'**
   - Pandas depends on NumPy. Install with: `pip3 install numpy --break-system-packages`

3. **KeyError when accessing a column**
   - Ensure the column name exists in the DataFrame and is spelled correctly.

4. **IndexError**
   - Make sure you are accessing valid row indices using loc or iloc.
