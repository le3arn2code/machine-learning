# Interview Q&A - Decision Tree Visualization

**Q1. What is the purpose of visualizing a decision tree?**
To interpret model decisions easily by showing how features are split and classified.

**Q2. What library is commonly used to visualize decision trees in Python?**
`Graphviz` (via `export_graphviz` and `graphviz.Source`).

**Q3. What does Gini impurity measure?**
It measures node impurity — how mixed the classes are within a node.

**Q4. What is the difference between Gini and Entropy criteria?**
Gini focuses on misclassification rate, while Entropy uses information gain to determine splits.

**Q5. Why do we use 'filled=True' in export_graphviz()?**
It colors the nodes based on class distribution for better visual interpretation.

**Q6. What is the significance of leaf nodes?**
Leaf nodes represent final classification outcomes where no further splitting occurs.

**Q7. How can you export a decision tree as an image or PDF?**
Use:
```python
graph.render("tree_name")
```
after creating a `graphviz.Source` object.

**Q8. How do you interpret sample and value fields in nodes?**
- `samples`: Number of data points at that node.
- `value`: Distribution of class labels.

**Q9. What are some common reasons Graphviz visualization fails?**
- Missing Graphviz executables (`dot` not installed).
- File path permission issues.
- Wrong file extension or out_file parameter.

**Q10. What’s a practical use of decision tree visualization in real life?**
Used in business decision support systems, fraud detection, and credit scoring for transparency and explainability.
