# Troubleshooting - Lab 48 (Text Vectorization)

### 1. ModuleNotFoundError: scikit-learn
**Fix:**
```bash
pip install scikit-learn --break-system-packages
```

### 2. ImportError: numpy or pandas missing
**Fix:**
```bash
pip install numpy pandas --break-system-packages
```

### 3. Empty TF-IDF Matrix
If values are all zeros, ensure diverse, non-repetitive input text.
