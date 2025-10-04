# Interview Q&A - Lab 29

1. What is k-fold cross-validation?
   - Divides data into k parts for training/testing multiple times.

2. Why use cross-validation?
   - Gives a more accurate model performance estimate.

3. Why shuffle data in KFold?
   - To randomize splits and avoid sequence bias.

4. Typical values for k?
   - Usually 5 or 10.

5. What metric did we use here?
   - Accuracy Score.

6. How to evaluate variance in results?
   - Compare accuracies across folds.

7. What indicates overfitting?
   - Large differences between training and validation accuracy.

8. What is StratifiedKFold?
   - Ensures class distribution consistency in splits.

9. What library automates cross-validation?
   - scikit-learn’s cross_val_score.

10. When to use cross-validation?
    - During model evaluation and hyperparameter tuning.
