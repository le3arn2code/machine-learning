# Interview Q&A: Decision Trees in Machine Learning

**1. What is a Decision Tree?**  
A Decision Tree is a supervised learning algorithm used for classification and regression tasks. It splits data into branches based on feature conditions to reach a decision at the leaf nodes.

**2. What is the difference between Gini Index and Entropy?**  
- **Gini Index** measures impurity by calculating how often a randomly chosen element would be incorrectly labeled.  
- **Entropy** measures the information content or disorder in the dataset. Lower entropy means higher purity.

**3. How does a Decision Tree decide which feature to split on?**  
The algorithm chooses the feature that provides the highest information gain or lowest Gini impurity for a given node.

**4. What are the advantages of Decision Trees?**  
- Easy to understand and visualize  
- Requires little data preprocessing  
- Can handle both numerical and categorical data

**5. What are the disadvantages of Decision Trees?**  
- Prone to overfitting  
- Sensitive to small changes in data  
- High variance

**6. What is feature importance in Decision Trees?**  
Feature importance shows how much each feature contributes to the decision-making process based on impurity reduction.

**7. How can overfitting be prevented in Decision Trees?**  
- Use **pruning**  
- Limit tree depth (`max_depth`)  
- Set a minimum number of samples for splits (`min_samples_split`)

**8. What is pruning in Decision Trees?**  
Pruning removes branches that have little importance to reduce overfitting and improve generalization.

**9. How do Decision Trees handle missing data?**  
They can either ignore missing values, use surrogate splits, or impute them during preprocessing.

**10. What is the difference between Decision Trees and Random Forests?**  
A Decision Tree is a single model, while a Random Forest is an ensemble of multiple Decision Trees that reduces overfitting by averaging results.
