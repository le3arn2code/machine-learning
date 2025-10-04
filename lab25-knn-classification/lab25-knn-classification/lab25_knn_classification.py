import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Load dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

print("First 5 rows of the dataset:")
print(data.head(), "\n")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('target', axis=1), data['target'], test_size=0.2, random_state=42
)

# Train and evaluate for multiple k values
accuracies = []
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    accuracies.append(acc)
    print(f"Accuracy with k={k}: {acc:.2f}")

# Plot results
plt.plot(range(1, 11), accuracies, marker='o')
plt.xlabel('k value')
plt.ylabel('Accuracy')
plt.title('k-NN Varying k Performance')
plt.savefig('lab25_knn_accuracy.png')
plt.close()
print("\n✅ Plot saved as lab25_knn_accuracy.png")
