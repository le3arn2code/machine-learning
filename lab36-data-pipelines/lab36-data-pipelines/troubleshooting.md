# Troubleshooting Guide - Lab 36

**Issue 1: sklearn ImportError**
- Ensure scikit-learn is installed: `pip install scikit-learn`

**Issue 2: LogisticRegression convergence warning**
- Increase max_iter value in the pipeline, e.g., `LogisticRegression(max_iter=300)`

**Issue 3: Missing pandas or numpy**
- Run: `pip install pandas numpy`

**Issue 4: Unexpected test score variations**
- This may happen due to random data splits; use `random_state=42` for consistency.
