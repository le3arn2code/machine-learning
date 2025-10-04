#!/usr/bin/env python3
"""Lab 33: Feature Engineering in Python"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

print("\n--- Task 1: Identify Potential New Features ---\n")

# Create sample dataset
data = {
    'feature1': [10, 20, 30, 40, 50],
    'feature2': [2, 4, 6, 8, 10],
    'existing_feature': [5, 10, 15, 20, 25],
    'target': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
print("Sample dataset loaded successfully:\n")
print(df.head())

# Save pairplot instead of showing
print("\nSaving pairplot visualization (pairplot.png)...")
sns.pairplot(df)
plt.savefig("pairplot.png")
plt.close()

print("\n--- Task 2: Create New Features Using Mathematical Operations ---\n")

# Mathematical transformations
print("Applying mathematical transformations...")
df['feature_square'] = df['existing_feature'] ** 2
df['feature_log'] = np.log1p(df['existing_feature'])
print(df[['existing_feature', 'feature_square', 'feature_log']])

# Interaction features
print("\nCreating interaction features...")
df['feature_interaction'] = df['feature1'] * df['feature2']
print(df[['feature1', 'feature2', 'feature_interaction']])

print("\n--- Task 3: Assess Feature Relevance ---\n")

# Correlation heatmap
print("Calculating correlation matrix and saving as heatmap.png...")
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Feature importance
print("\nTraining Random Forest model for feature importance...")
X = df.drop('target', axis=1)
y = df['target']
model = RandomForestRegressor(random_state=1)
model.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values(by='importance', ascending=False)

print("\nFeature Importance:\n")
print(feature_importance)

plt.figure(figsize=(8,4))
sns.barplot(x='importance', y='feature', data=feature_importance, palette='viridis')
plt.title("Feature Importance (Random Forest)")
plt.savefig("feature_importance.png")
plt.close()

print("\nAll visualizations saved successfully!\n")
