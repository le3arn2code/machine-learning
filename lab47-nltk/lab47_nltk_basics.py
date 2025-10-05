#!/usr/bin/env python3
# ============================================================
# Lab 47: Natural Language Processing Basics with NLTK
# ============================================================

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os

# Ensure required resources are downloaded automatically
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# ---- Task 2: Tokenize a Sample Text ----
sample_text = (
    "Natural Language Processing (NLP) enables computers to understand "
    "and communicate in human language. It's an exciting field!"
)

# Sentence Tokenization
sentences = sent_tokenize(sample_text)
print("\nSentence Tokenization:")
print(sentences)

# Word Tokenization
words = word_tokenize(sample_text)
print("\nWord Tokenization:")
print(words)

# ---- Task 3: Basic Text Preprocessing ----
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nAfter Stopword Removal:")
print(filtered_words)

ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]
print("\nAfter Stemming:")
print(stemmed_words)

# ---- Save Example Output ----
with open("screenshots/lab47_output.txt", "w") as f:
    f.write("Sentence Tokenization:\n")
    f.write(str(sentences) + "\n\n")
    f.write("Word Tokenization:\n")
    f.write(str(words) + "\n\n")
    f.write("Filtered Words:\n")
    f.write(str(filtered_words) + "\n\n")
    f.write("Stemmed Words:\n")
    f.write(str(stemmed_words) + "\n")

print("\n✅ Lab 47 completed successfully. Output saved to screenshots/lab47_output.txt.")
