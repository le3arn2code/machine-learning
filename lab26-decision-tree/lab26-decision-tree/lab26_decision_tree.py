# Lab 26: Introduction to Decision Trees for Machine Learning
# -----------------------------------------------------------
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Headless mode for remote/cloud environments
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Task 2: Explore Tree Structure
tree_rules = export_text(clf, feature_names=iris['feature_names'])
print("\nDecision Tree Rules:\n")
print(tree_rules)

# Task 3: Split Criteria and Feature Importance
print("\nFeature Importance (Gini Criterion):")
importance = clf.feature_importances_
feature_importance_df = pd.DataFrame(
    importance, index=iris['feature_names'], columns=["Importance"]
)
print(feature_importance_df.sort_values(by="Importance", ascending=False))

# Train using Entropy criterion
clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_entropy.fit(X_train, y_train)

# Plot Decision Tree
plt.figure(figsize=(18, 10))
plot_tree(
    clf, filled=True,
    feature_names=iris['feature_names'],
    class_names=iris['target_names']
)
plt.title("Decision Tree Visualization (Gini Criterion)")
plt.savefig("lab26_decision_tree.png", bbox_inches="tight")
print("\n✅ Tree plot saved as lab26_decision_tree.png")
