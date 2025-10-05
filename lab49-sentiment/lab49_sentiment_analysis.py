#!/usr/bin/env python3
# ============================================================
# Lab 49: Introduction to Sentiment Analysis with Python
# ============================================================

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import os

# ---- Setup ----
os.makedirs("screenshots", exist_ok=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# ---- Task 1: Prepare a Labeled Text Dataset ----
data = {
    "text": [
        "I love this movie! It’s fantastic and full of surprises.",
        "This was the worst film I have ever seen.",
        "Absolutely wonderful experience, would watch again!",
        "I didn’t like the plot. It was boring and predictable.",
        "The performances were brilliant, and the story was touching."
    ],
    "sentiment": ["positive", "negative", "positive", "negative", "positive"]
}

df = pd.DataFrame(data)
print("\nSample Dataset:")
print(df.head())

# ---- Task 1.2: Data Preprocessing ----
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

df["cleaned_text"] = df["text"].apply(clean_text)
print("\nCleaned Text Samples:")
print(df[["text", "cleaned_text"]].head())

# ---- Task 1.3: Split into Training and Test Sets ----
X_train, X_test, y_train, y_test = train_test_split(
    df["cleaned_text"], df["sentiment"], test_size=0.2, random_state=42
)
print(f"\nTraining Samples: {len(X_train)} | Testing Samples: {len(X_test)}")

# ---- Task 2: Train a Simple Sentiment Classifier ----
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# ---- Task 3: Evaluate Sentiment Predictions ----
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n", report)

# ---- Save Results ----
with open("screenshots/lab49_output.txt", "w") as f:
    f.write("=== Sentiment Analysis Report ===\n\n")
    f.write("Accuracy: " + str(accuracy) + "\n\n")
    f.write(report + "\n")

print("\n✅ Lab 49 completed successfully. Results saved to screenshots/lab49_output.txt.")
