# Lab 19: Data Preprocessing with scikit-learn - Scaling

## Objectives
- Understand the importance of data scaling in machine learning.
- Learn how to use scikit-learn's `StandardScaler` to scale data.
- Compare the impact of scaled and unscaled data on machine learning models.

## Tasks
### Task 1: Import StandardScaler
- Imported required libraries (`numpy`, `pandas`, `StandardScaler`).

### Task 2: Scale a Sample Dataset
- Created a small dataset with two features.
- Applied `StandardScaler`.
- Verified scaled data has mean ≈ 0 and std ≈ 1.

### Task 3: Compare Scaled vs Unscaled Data
- Displayed summary statistics of original vs scaled data.
- Visualized both datasets using bar plots.

## Conclusion
Scaling ensures features contribute equally by normalizing values. This is critical for ML algorithms that use distance measures like SVM and KNN.
