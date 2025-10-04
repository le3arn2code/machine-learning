# Troubleshooting Guide

### 1️⃣ ModuleNotFoundError
If scikit-learn or pandas is missing:
pip install scikit-learn pandas numpy

### 2️⃣ ImportError (version mismatch)
Ensure your Python is 3.8+ and scikit-learn >= 1.0.

### 3️⃣ Accuracy values not matching
This may vary slightly due to randomization; set `random_state=42` to ensure reproducibility.
