# Troubleshooting - Lab 49 (Sentiment Analysis)

### 1. LookupError: NLTK resource not found
**Fix:**
```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

### 2. ModuleNotFoundError: scikit-learn or pandas
**Fix:**
```bash
pip install scikit-learn pandas --break-system-packages
```

### 3. Low Accuracy
This can happen due to a small dataset. Try adding more samples to balance classes.
