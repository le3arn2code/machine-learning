#!/usr/bin/env python3
# ============================================================
# Lab 48: Text Vectorization with CountVectorizer and TF-IDF
# ============================================================

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import os

# ---- Setup ----
os.makedirs("screenshots", exist_ok=True)

# ---- Task 1: CountVectorizer on Sample Text ----
documents = [
    "Text analysis is an interesting field.",
    "Machine Learning is part of data science.",
    "Text analysis involves understanding data."
]

# Initialize and fit CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nVectorized Data (Counts):")
print(X.toarray())

# ---- Task 2: TF-IDF Transformation ----
tfidf_transformer = TfidfTransformer()
tfidf_matrix = tfidf_transformer.fit_transform(X)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# ---- Save results to file ----
output_path = "screenshots/lab48_output.txt"
with open(output_path, "w") as f:
    f.write("Vocabulary:\n")
    f.write(str(vectorizer.get_feature_names_out()) + "\n\n")
    f.write("CountVectorizer Matrix:\n")
    f.write(str(X.toarray()) + "\n\n")
    f.write("TF-IDF Matrix:\n")
    f.write(str(tfidf_matrix.toarray()) + "\n")

print(f"\n✅ Lab 48 completed successfully. Results saved to {output_path}")
