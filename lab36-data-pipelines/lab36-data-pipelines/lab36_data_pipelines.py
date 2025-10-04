#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

print("\n--- Task 1: Build a Pipeline with Preprocessing Steps ---")
data = load_iris()
X, y = data.data, data.target
print("\nLoaded Iris dataset successfully!")
print("Feature shape:", X.shape)
print("Target classes:", np.unique(y))

preprocessing_steps = [
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
]
preprocessing_pipeline = Pipeline(preprocessing_steps)
print("\nPreprocessing pipeline created with steps:")
for name, step in preprocessing_pipeline.steps:
    print(f" - {name}: {step.__class__.__name__}")

print("\n--- Task 2: Integrate Model Training into the Pipeline ---")
model_pipeline = Pipeline([
    ('preprocessing', preprocessing_pipeline),
    ('classifier', LogisticRegression(max_iter=200))
])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nData split completed: {X_train.shape[0]} training samples, {X_test.shape[0]} test samples")

print("\n--- Task 3: Evaluate the Complete Pipeline ---")
scores = cross_val_score(model_pipeline, X_train, y_train, cv=5)
print("Cross-validation scores:", scores)
print("Mean cross-validation score: {:.2f}".format(scores.mean()))

model_pipeline.fit(X_train, y_train)
test_score = model_pipeline.score(X_test, y_test)
print("Test set score: {:.2f}".format(test_score))

print("\n--- Lab 36 Completed Successfully ---")
print("You have built, trained, and evaluated a complete ML pipeline using scikit-learn.")
print("✔ Preprocessing automated")
print("✔ Model integrated")
print("✔ Performance evaluated with cross-validation")
