# Troubleshooting - Lab 14

## Error: `ModuleNotFoundError: No module named 'pandas'`
- Fix: Install pandas using `pip install pandas --break-system-packages`

## Error: `ModuleNotFoundError: No module named 'missingno'`
- Fix: Install missingno using `pip install missingno --break-system-packages`

## Error: `FileNotFoundError: 'your_file.csv'`
- Fix: Ensure you create `sample.csv` inside the script or provide the correct CSV path.

## Warning: `FutureWarning: inplace will be deprecated`
- Fix: Instead of `df['col'].fillna(..., inplace=True)`, use:
```python
df['col'] = df['col'].fillna(...)
```
