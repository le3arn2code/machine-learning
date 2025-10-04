# Troubleshooting

- **ModuleNotFoundError: sklearn**
  ```bash
  pip install scikit-learn --break-system-packages
  ```
- **Incorrect test_size**
  Ensure test_size is between 0 and 1 (e.g., 0.2).
- **Stratify errors**
  Make sure y is a 1D label array.
