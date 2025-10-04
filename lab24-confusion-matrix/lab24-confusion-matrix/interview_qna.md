# Interview Q&A: Confusion Matrix and Model Evaluation

**Q1. What is a confusion matrix?**
A confusion matrix summarizes classification results by comparing predicted and actual labels.

**Q2. Define TP, FP, TN, FN.**
- TP: Correctly predicted positives
- FP: Incorrectly predicted positives
- TN: Correctly predicted negatives
- FN: Incorrectly predicted negatives

**Q3. Key metrics:**
- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

**Q4. When to use Precision vs Recall?**
Precision matters when False Positives are costly (e.g., spam detection).  
Recall matters when False Negatives are costly (e.g., disease diagnosis).
