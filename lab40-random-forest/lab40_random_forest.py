
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("\n--- Task 1: Train a Random Forest on a Sample Dataset ---")
iris = load_iris()
X, y = iris.data, iris.target
print("Dataset loaded successfully.")
print("Features:", iris.feature_names)
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of target classes:", len(iris.target_names))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("✔ Dataset split into 70% training and 30% testing sets.")

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
print("✔ Random Forest model trained successfully with 100 estimators.")

print("\n--- Task 2: Evaluate the Model Performance ---")
y_pred = rf_model.predict(X_test)
print("✔ Predictions made successfully on test data.")

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n--- Task 3: Explore Feature Importances ---")
importances = rf_model.feature_importances_
feature_names = iris.feature_names
feature_importance_df = pd.DataFrame({'feature': feature_names, 'importance': importances}).sort_values(by='importance', ascending=False)
print("\nFeature Importances (sorted):")
print(feature_importance_df)

plt.figure(figsize=(8, 5))
sns.barplot(x='importance', y='feature', data=feature_importance_df, palette='viridis')
plt.title('Feature Importances in Random Forest')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig('feature_importances.png')
plt.close()

print("\nSaving feature importance visualization (feature_importances.png)...")
print("\n--- Lab 40 Completed Successfully ---")
print("✔ Random Forest model trained and evaluated.")
print("✔ Feature importances analyzed and visualized.")
