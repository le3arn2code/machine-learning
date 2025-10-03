import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {'Category': ['Apple', 'Banana', 'Cherry', 'Apple', 'Cherry', 'Banana']}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# Label Encoding
label_encoder = LabelEncoder()
df['Category_encoded'] = label_encoder.fit_transform(df['Category'])
print("\nLabel Encoded Data:\n", df)
