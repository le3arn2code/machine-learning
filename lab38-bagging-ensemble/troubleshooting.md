# Troubleshooting Guide

**Issue:** `TypeError: BaggingClassifier() got an unexpected keyword argument 'base_estimator'`
- **Cause:** scikit-learn version >= 1.6 uses `estimator` instead of `base_estimator`.
- **Fix:** The provided script auto-detects and adjusts based on version.

**Issue:** `ModuleNotFoundError: No module named 'sklearn'`
- **Fix:** Run `pip install scikit-learn numpy pandas`

**Issue:** Accuracy shows 1.0 for both models
- **Explanation:** Iris dataset is simple; both models can perfectly classify.
