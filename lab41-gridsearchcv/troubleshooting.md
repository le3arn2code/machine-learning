# Troubleshooting Guide

- **Issue:** ModuleNotFoundError for sklearn or pandas
  **Fix:** Run `pip install scikit-learn pandas matplotlib`

- **Issue:** Slow grid search
  **Fix:** Use fewer parameter combinations or set `n_jobs=-1` to parallelize.

- **Issue:** No improvement in accuracy
  **Fix:** Try expanding parameter grid or switching model.
