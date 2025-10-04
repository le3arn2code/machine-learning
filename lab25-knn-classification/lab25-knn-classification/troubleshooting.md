# Troubleshooting

## Common Issues

### 1. Font Cache Warning
- When running matplotlib for the first time, you might see: 
  "Matplotlib is building the font cache; this may take a moment."
- This is normal and occurs only once.

### 2. Running in Headless Mode (Cloud/CLI Environment)
- Ensure matplotlib is set to headless mode:
  ```python
  import matplotlib
  matplotlib.use('Agg')
  ```

### 3. Plot Display Issues
- Use `plt.savefig("lab25_knn_accuracy.png")` instead of `plt.show()` for remote or server environments.
- Always close figures after saving to avoid memory buildup:
  ```python
  plt.close()
  ```
