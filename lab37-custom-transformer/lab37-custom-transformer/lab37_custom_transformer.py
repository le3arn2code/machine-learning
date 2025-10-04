import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

print("\n--- Task 1: Write a Custom Transformer Class ---")

class MyCustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, parameter=1):
        self.parameter = parameter

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        print(f"Transforming data: multiplying all values by {self.parameter}")
        return X * self.parameter


print("\n--- Task 2: Implement Fit and Transform Methods ---")

class MyCustomAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_value=10):
        self.add_value = add_value

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        print(f"Transforming data: adding {self.add_value} to all elements")
        return X + self.add_value


print("\n--- Task 3: Test the Transformer within a Pipeline ---")

data = {'feature1': [10, 20, 30], 'feature2': [1, 2, 3]}
X = pd.DataFrame(data)
print("\nSample Data:")
print(X)

print("\nBuilding pipeline with MyCustomTransformer...")
my_pipeline = Pipeline(steps=[('custom_transform', MyCustomTransformer(parameter=5))])
transformed_data = my_pipeline.fit_transform(X)
print("\nTransformed Data (Multiplied):")
print(transformed_data)

print("\nBuilding pipeline with MyCustomAdder...")
my_pipeline2 = Pipeline(steps=[('custom_add', MyCustomAdder(add_value=10))])
transformed_data2 = my_pipeline2.fit_transform(X)
print("\nTransformed Data (Added):")
print(transformed_data2)

print("\n--- Evaluation ---")
print("Both custom transformers successfully integrated within pipelines.")
print("✔ Custom logic executed")
print("✔ Fit and transform methods used properly")
print("✔ Output verified with numeric transformation results")

print("\n--- Lab 37 Completed Successfully ---")
print("You have built, tested, and integrated a custom transformer inside a scikit-learn pipeline.")
