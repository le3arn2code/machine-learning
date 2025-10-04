import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import matplotlib.pyplot as plt

# Load the dataset
data = load_iris()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model using Joblib
joblib.dump(model, "random_forest_model.pkl")
print("✅ Model saved successfully as random_forest_model.pkl")

# Load the saved model
loaded_model = joblib.load("random_forest_model.pkl")

# Make predictions with the loaded model
predictions = loaded_model.predict(X_test)
print("Predicted Labels:", predictions)
print("Actual Labels:   ", y_test)

# Headless plotting (close all)
plt.close()
