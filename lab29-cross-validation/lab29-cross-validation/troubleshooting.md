# Troubleshooting - Lab 29

## 1. sklearn not found
pip install scikit-learn --break-system-packages

## 2. ConvergenceWarning
Use model = LogisticRegression(max_iter=500)

## 3. Accuracy inconsistency
Check random_state and ensure data shuffling is enabled.
