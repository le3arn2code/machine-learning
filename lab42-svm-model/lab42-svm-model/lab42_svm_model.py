#!/usr/bin/env python3
# Lab 42: Building and Evaluating a Support Vector Machine Model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

print("\n--- Task 1: Train an SVM Model Using scikit-learn ---")
iris = datasets.load_iris()
X, y = iris.data, iris.target
print("✅ Dataset loaded successfully.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train, X_test = scaler.fit_transform(X_train), scaler.transform(X_test)
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)
print("✅ SVM model trained successfully using RBF kernel.")

print("\n--- Task 2: Evaluate Performance Metrics ---")
y_pred = svm_model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("\n--- Task 3: Experiment with Different Kernel Parameters ---")
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train, y_train)
print("\nLinear Kernel Performance:\n", classification_report(y_test, svm_linear.predict(X_test), target_names=iris.target_names))

svm_poly = SVC(kernel='poly', degree=3, C=1.0, gamma='scale')
svm_poly.fit(X_train, y_train)
print("\nPolynomial Kernel Performance:\n", classification_report(y_test, svm_poly.predict(X_test), target_names=iris.target_names))

print("\nRBF Kernel Performance (baseline):\n", classification_report(y_test, y_pred, target_names=iris.target_names))
print("\n✅ All kernel variations trained and evaluated successfully.")
print("\n--- Lab 42 Completed Successfully ---")
