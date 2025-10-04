# Troubleshooting - Lab 30

## 1. ModuleNotFoundError: No module named 'joblib'
Install Joblib using:
```bash
pip install joblib --break-system-packages
```

## 2. Model file not found
Ensure you saved the model first using `joblib.dump()`.

## 3. Permissions issue
Change file permissions:
```bash
sudo chmod 777 random_forest_model.pkl
```

## 4. Scikit-learn version mismatch
Upgrade to the latest version:
```bash
pip install --upgrade scikit-learn
```
