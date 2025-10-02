# Troubleshooting Notes

## Issue 1: Python command not found
- **Cause**: Some systems use `python3` instead of `python`.
- **Resolution**: Use `python3 --version` and `python3 script.py`.

## Issue 2: Pip not installed
- **Cause**: Some Python installations do not include pip by default.
- **Resolution**: Install pip manually using package manager (apt/yum/brew) or ensure Python was installed with pip option enabled.

## Issue 3: Version mismatch of libraries
- **Cause**: Older pip installations might not fetch latest versions.
- **Resolution**: Upgrade pip using:
  ```bash
  python3 -m pip install --upgrade pip
  ```

## Final Working Commands
```bash
python3 --version
pip install numpy pandas scikit-learn
python3 hello_ml.py
```
