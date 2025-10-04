#!/usr/bin/env python3
# Lab 39: Introduction to Ensemble Methods — Boosting with Python

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import __version__ as sklearn_version

print("\n--- Task 1: Use AdaBoostClassifier on a Dataset ---")
print(f"✅ Libraries imported successfully. (scikit-learn version: {sklearn_version})")

iris = load_iris()
X, y = iris.data, iris.target
print(f"\nLoaded Iris dataset successfully.\nFeatures: {iris.feature_names}\nNumber of classes: {len(np.unique(y))}\nDataset shape: {X.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split completed into 70% train and 30% test sets.")

print("\n--- Task 2: Train and Evaluate the Boosting Model ---")
boosting_model = AdaBoostClassifier(n_estimators=50, random_state=42)
boosting_model.fit(X_train, y_train)
print("✅ AdaBoost model trained successfully with 50 estimators.")
y_pred = boosting_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"AdaBoost Model Accuracy: {accuracy:.2f}")

print("\n--- Task 3: Compare with Other Ensemble Methods ---")
bagging_model = BaggingClassifier(n_estimators=50, random_state=42)
bagging_model.fit(X_train, y_train)
y_pred_bag = bagging_model.predict(X_test)
accuracy_bag = accuracy_score(y_test, y_pred_bag)
print(f"Bagging Model Accuracy: {accuracy_bag:.2f}")

estimators = [('bagging', BaggingClassifier(n_estimators=10, random_state=42)),
              ('boosting', AdaBoostClassifier(n_estimators=10, random_state=42))]
stacking_model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
stacking_model.fit(X_train, y_train)
y_pred_stack = stacking_model.predict(X_test)
accuracy_stack = accuracy_score(y_test, y_pred_stack)
print(f"Stacking Model Accuracy: {accuracy_stack:.2f}")

improvement_boost_vs_bag = accuracy - accuracy_bag
improvement_boost_vs_stack = accuracy - accuracy_stack
print(f"\nImprovement in Accuracy (Boosting vs Bagging): {improvement_boost_vs_bag:.2f}")
print(f"Improvement in Accuracy (Boosting vs Stacking): {improvement_boost_vs_stack:.2f}")

print("\n--- Lab 39 Completed Successfully ---")
print("✅ You implemented AdaBoost using scikit-learn.")
print("✅ Compared boosting performance with Bagging and Stacking methods.")
print("✅ Observed how ensemble methods reduce bias/variance and improve robustness.")
