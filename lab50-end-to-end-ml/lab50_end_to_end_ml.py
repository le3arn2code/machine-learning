#!/usr/bin/env python3
# ============================================================
# Lab 50: Final Project - End-to-End ML Workflow in Python
# ============================================================

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("screenshots", exist_ok=True)

print("\nLoading Iris dataset...")
data = load_iris()
X, y = data.data, data.target
df = pd.DataFrame(X, columns=data.feature_names)
df["target"] = y
print(df.head())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Iris Classification")
plt.tight_layout()
plt.savefig("screenshots/lab50_confusion_matrix.png")
plt.close()

with open("screenshots/lab50_output.txt", "w") as f:
    f.write("=== End-to-End ML Workflow ===\n")
    f.write(f"Accuracy: {accuracy:.4f}\n\n")
    f.write("Confusion Matrix:\n")
    np.savetxt(f, cm, fmt="%d")

print("\n✅ Lab 50 completed successfully. Outputs saved to screenshots/.")
