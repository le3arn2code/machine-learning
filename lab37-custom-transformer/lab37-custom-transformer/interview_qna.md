### Interview Q&A

**Q1: Why do we need custom transformers?**  
A: To handle domain-specific preprocessing or transformations not covered by built-in tools.

**Q2: What methods must a scikit-learn transformer implement?**  
A: `fit()` and `transform()`. Optionally, `fit_transform()` can be inherited from `TransformerMixin`.

**Q3: Why integrate transformers in pipelines?**  
A: For modularity, reproducibility, and to prevent data leakage.

**Q4: What base classes are used for a custom transformer?**  
A: `BaseEstimator` and `TransformerMixin` from `sklearn.base`.
