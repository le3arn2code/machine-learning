# Interview Q&A - Lab 21: Linear Regression

**Q1. What is Linear Regression?**  
Linear Regression is a supervised ML algorithm that models the relationship between a dependent variable (target) and one or more independent variables (features) by fitting a linear equation.

**Q2. What is the difference between Simple and Multiple Linear Regression?**  
- Simple: one independent variable.  
- Multiple: multiple independent variables.

**Q3. What are MSE and R²?**  
- **MSE (Mean Squared Error):** Average squared difference between predicted and actual values. Lower = better.  
- **R² (Coefficient of Determination):** Proportion of variance explained by the model. Closer to 1 = better.

**Q4. What are the assumptions of Linear Regression?**  
1. Linearity  
2. Independence  
3. Homoscedasticity (equal variance)  
4. Normality of residuals

**Q5. How can overfitting occur in Linear Regression?**  
Overfitting occurs when the model learns noise along with the signal. It can be mitigated with **regularization** (Lasso, Ridge), cross-validation, or simpler models.
