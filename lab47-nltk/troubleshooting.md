# Troubleshooting - Lab 47 (NLTK Basics)

## ⚠️ Common Issues

### 1. Missing Tokenizer Resources
If you get this error:
```
LookupError: Resource punkt_tab not found.
```
**Fix:**
Add the following lines at the start of your script:
```python
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

### 2. Permission Denied
If you cannot create `/screenshots/`:
```
mkdir -p screenshots
```

### 3. Slow First Run
NLTK downloads resources the first time — subsequent runs will be instant.

✅ After fixing, re-run:
```
python3 lab47_nltk_basics.py
```
