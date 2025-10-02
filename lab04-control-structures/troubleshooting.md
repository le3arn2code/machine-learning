# Troubleshooting

## Common Issues and Fixes

### 1. Wrong filename or typo
- **Cause:** Typing errors when running the script.
- **Fix:** Double-check filenames, e.g., `lab04_if.py` not `lab4if.py`.

### 2. Python version mismatch
- **Cause:** Running with `python` defaulting to Python 2.
- **Fix:** Always run with `python3`.

### 3. Input errors
- **Cause:** Entering non-numeric input in `lab04_input_check.py` caused ValueError.
- **Fix:** Ensure only numbers are entered, or add error handling with try/except.

### 4. Infinite loop risk
- **Cause:** Forgetting to increment counter in `while` loop leads to infinite loop.
- **Fix:** Always update the counter inside the loop.
