"""
Lab 31 - Basic Data Augmentation using Python
Using real image: image_2025-06-03_161241346.png
"""

from PIL import Image
import numpy as np
import nltk
from nltk.corpus import wordnet
import matplotlib.pyplot as plt
import os

# ---------------- IMAGE AUGMENTATION ----------------
image_path = "image_2025-06-03_161241346.png"

if os.path.exists(image_path):
    print(f"✅ Found image: {image_path}")
    image = Image.open(image_path)

    # Rotate image and save
    rotated_image = image.rotate(90)
    rotated_image.save("rotated_image.png")
    print("✅ Saved rotated image as rotated_image.png")

    # Flip image horizontally and save
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save("flipped_image.png")
    print("✅ Saved flipped image as flipped_image.png")
else:
    print(f"⚠️ Image not found at {image_path}. Please check the path.")

# ---------------- TEXT AUGMENTATION ----------------
nltk.download('wordnet', quiet=True)

text = "Data augmentation is a technique to expand dataset diversity."

def synonym_replacement(text, n):
    words = text.split()
    new_words = words.copy()
    for i in range(n):
        word_to_replace = new_words[i % len(new_words)]
        synonyms = [syn.lemmas()[0].name() for syn in wordnet.synsets(word_to_replace)]
        if synonyms:
            new_words[i % len(new_words)] = synonyms[0]
    return ' '.join(new_words)

new_text = synonym_replacement(text, 2)
print("📝 Augmented Text:", new_text)

with open("augmented_text.txt", "w") as f:
    f.write(new_text)
print("✅ Saved augmented text to augmented_text.txt")

plt.close()
