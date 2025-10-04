# Troubleshooting - Lab 31

## 1. FileNotFoundError
Ensure the image file `image_2025-06-03_161241346.png` exists in the working directory.

## 2. Missing Libraries
Install using:
```bash
pip install Pillow numpy opencv-python nltk --break-system-packages
```

## 3. NLTK WordNet not found
Run:
```python
import nltk
nltk.download('wordnet')
```

## 4. Display not supported
Comment out `.show()` calls if running on headless systems like EC2 or WSL.
