# Troubleshooting - Lab 23

1. **Font cache delay**  
   First matplotlib run may take time to build the font cache.

2. **Headless VM**  
   Always use:
   ```python
   import matplotlib
   matplotlib.use("Agg")
   ```
   so no GUI display is required.

3. **Perfect Accuracy (1.00)**  
   Since only 2 easily separable classes are used, Logistic Regression may achieve 100% accuracy.
