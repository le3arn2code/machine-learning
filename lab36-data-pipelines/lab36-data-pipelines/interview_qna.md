# Interview Q&A - Data Pipelines with scikit-learn

**Q1: What is a Pipeline in scikit-learn?**
A pipeline sequentially applies data transformations and model training, simplifying the ML workflow.

**Q2: Why use Pipelines?**
They ensure reproducibility, cleaner code, and easier hyperparameter tuning.

**Q3: Can you include feature engineering in a Pipeline?**
Yes, additional preprocessing or custom transformers can be added as pipeline steps.

**Q4: How is cross-validation integrated with Pipelines?**
`cross_val_score()` runs the entire pipeline (including preprocessing and training) for each fold, ensuring consistent evaluation.

**Q5: What are common pipeline components?**
- `Imputer` for handling missing values
- `Scaler` for normalization
- `Estimator` for model fitting (e.g., LogisticRegression, RandomForest)
