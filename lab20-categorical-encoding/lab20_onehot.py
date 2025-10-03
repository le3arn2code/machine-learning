import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
data = {'Category': ['Apple', 'Banana', 'Cherry', 'Apple', 'Cherry', 'Banana']}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# One-Hot Encoding
onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(df[['Category']])
categories = onehot_encoder.get_feature_names_out(['Category'])
df_onehot = pd.DataFrame(onehot_encoded, columns=categories)
print("\nOne-Hot Encoded Data:\n", df_onehot)
