import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = {'Category': ['Apple', 'Banana', 'Cherry', 'Apple', 'Cherry', 'Banana']}
df = pd.DataFrame(data)

# Sample target labels
y = [0, 1, 0, 1, 0, 1]

# Define categorical features
categorical_features = ['Category']
categorical_transformer = OneHotEncoder(sparse_output=False)

# Build preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[('cat', categorical_transformer, categorical_features)]
)

# Full pipeline with Logistic Regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Train pipeline
pipeline.fit(df[['Category']], y)

# Predictions
preds = pipeline.predict(df[['Category']])
print("Original Data:\n", df)
print("\nPredictions:", preds)
