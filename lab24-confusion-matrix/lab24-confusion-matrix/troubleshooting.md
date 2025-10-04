# Troubleshooting Guide

- If Matplotlib shows display errors, use headless mode:
  ```python
  import matplotlib
  matplotlib.use("Agg")
  ```

- Ensure you close plots after saving:
  ```python
  plt.close()
  ```

- If `sns` or `sklearn` not found, install them:
  ```bash
  pip install seaborn scikit-learn matplotlib pandas numpy
  ```
