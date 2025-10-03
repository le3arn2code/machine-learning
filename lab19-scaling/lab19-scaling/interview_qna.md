# Interview Q&A - Lab 19 Scaling

**Q1: Why is data scaling important?**  
A1: Because features with larger ranges can dominate distance-based algorithms like KNN or SVM. Scaling standardizes features to a similar scale.

**Q2: What does StandardScaler do?**  
A2: It transforms features such that each has mean 0 and standard deviation 1.

**Q3: What are alternatives to StandardScaler?**  
A3: - MinMaxScaler: Scales features to a fixed range (default 0–1).  
    - RobustScaler: Uses median and IQR, robust to outliers.  
    - Normalizer: Normalizes samples individually to unit norm.

**Q4: Which models are sensitive to scaling?**  
A4: KNN, SVM, Logistic Regression, Neural Networks. Models like decision trees and random forests are not sensitive.

**Q5: Why compare scaled vs unscaled data?**  
A5: To visually and statistically observe how scaling changes distributions and ensures fair feature contribution.
