# Lab 23: Logistic Regression for Classification

import matplotlib
matplotlib.use("Agg")  # Headless mode for cloud VM
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Use only classes 0 and 1 for binary classification
X = X[y != 2]
y = y[y != 2]

print("Dataset Shape:", X.shape)
print("First 5 rows:")
print(X.head(), "\n")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save accuracy to file
with open("accuracy.txt", "w") as f:
    f.write(f"Model Accuracy: {accuracy:.2f}\n")
