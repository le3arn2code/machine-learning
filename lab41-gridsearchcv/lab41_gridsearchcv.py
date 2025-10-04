import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

print("\n--- Task 1: Define a Parameter Grid for a Model ---")
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Dataset loaded and split successfully.")

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
model = SVC()
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', verbose=2, n_jobs=-1)
grid_search.fit(X_train, y_train)

print("\n--- Task 3: Evaluate and Select the Best Parameters ---")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.2f}")

best_model = grid_search.best_estimator_
test_accuracy = best_model.score(X_test, y_test)
print(f"Test Set Accuracy: {test_accuracy:.2f}\n")

y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Plot accuracy trends
results = grid_search.cv_results_
plt.plot(results['mean_test_score'])
plt.title('GridSearchCV Mean Test Accuracy per Parameter Combination')
plt.xlabel('Parameter Combination Index')
plt.ylabel('Mean Test Accuracy')
plt.savefig('gridsearchcv_results.png')
print("Saved grid search accuracy plot as gridsearchcv_results.png")
