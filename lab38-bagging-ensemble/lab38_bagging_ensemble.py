#!/usr/bin/env python3
# Lab 38: Introduction to Ensemble Methods - Bagging with Python

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import sklearn

print("\n--- Task 1: Use BaggingClassifier with a Base Estimator ---")
print(f"✅ Libraries imported successfully. (scikit-learn version: {sklearn.__version__})")

iris = load_iris()
X, y = iris.data, iris.target
print("\n--- Task 2: Train on a Sample Dataset ---")
print(f"Loaded Iris dataset successfully. Shape: {X.shape}, Target classes: {np.unique(y)}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split completed into 70% train and 30% test sets.")

base_estimator = DecisionTreeClassifier(random_state=42)
if "estimator" in BaggingClassifier().get_params():
    bagging_clf = BaggingClassifier(estimator=base_estimator, n_estimators=10, random_state=42)
else:
    bagging_clf = BaggingClassifier(base_estimator=base_estimator, n_estimators=10, random_state=42)

bagging_clf.fit(X_train, y_train)
print("✅ BaggingClassifier trained successfully with 10 Decision Trees.")
y_pred = bagging_clf.predict(X_test)
bagging_accuracy = accuracy_score(y_test, y_pred)
print(f"Bagging Classifier Accuracy: {bagging_accuracy:.2f}")

print("\n--- Task 3: Compare Results with a Single Estimator ---")
single_tree_clf = DecisionTreeClassifier(random_state=42)
single_tree_clf.fit(X_train, y_train)
print("Single Decision Tree model trained successfully.")

y_single_pred = single_tree_clf.predict(X_test)
single_accuracy = accuracy_score(y_test, y_single_pred)
print(f"Single Decision Tree Accuracy: {single_accuracy:.2f}")
print(f"Improvement in Accuracy (Bagging vs Single Tree): {bagging_accuracy - single_accuracy:.2f}")

print("\n--- Lab 38 Completed Successfully ---")
print("✔️ You implemented Bagging using scikit-learn.")
print("✔️ Compared ensemble performance with a single Decision Tree.")
print("✔️ Observed how ensemble methods reduce variance and improve stability.")
