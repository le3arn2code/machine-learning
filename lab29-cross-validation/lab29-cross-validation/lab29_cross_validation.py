from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# K-Fold Cross Validation setup
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
model = LogisticRegression(max_iter=200)

accuracies = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    accuracies.append(accuracy)

print("Accuracies for each fold:", accuracies)
average_accuracy = np.mean(accuracies)
print(f"Average accuracy across {k} folds: {average_accuracy:.4f}")
plt.close()
