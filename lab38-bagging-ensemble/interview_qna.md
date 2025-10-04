# Interview Q&A: Bagging Ensemble

**Q1:** What is Bagging?  
**A:** Bagging (Bootstrap Aggregating) trains multiple models on random subsets of data and averages their predictions to reduce variance.

**Q2:** Why does Bagging improve performance?  
**A:** It reduces overfitting by averaging multiple models trained on different data samples.

**Q3:** What’s the difference between Bagging and Boosting?  
**A:** Bagging trains models independently and averages results, while Boosting trains models sequentially with each focusing on previous errors.

**Q4:** Can Bagging be applied to regression problems?  
**A:** Yes, via `BaggingRegressor` in scikit-learn.

**Q5:** When would you *not* use Bagging?  
**A:** When the base model already has low variance, as Bagging mostly helps reduce variance, not bias.
