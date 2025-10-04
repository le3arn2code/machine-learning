# Lab 27: Visualizing Decision Trees
# ----------------------------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
import graphviz

print("✅ Dataset loaded successfully.")

iris = load_iris()
X, y = iris.data, iris.target

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)

# Train model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)
print("\nModel trained successfully!")

# Matplotlib visualization
plt.figure(figsize=(12, 6))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title("Decision Tree Visualization (Iris Dataset)")
plt.savefig("lab27_tree_matplotlib.png", bbox_inches="tight")
plt.close()

# Graphviz visualization
dot_data = export_graphviz(
    clf, out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True, rounded=True,
    special_characters=True
)
graph = graphviz.Source(dot_data)
graph.render("lab27_iris_tree")
print("✅ PDF and PNG generated successfully.")
