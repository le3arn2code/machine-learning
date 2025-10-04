# Troubleshooting Notes

1. **Matplotlib Display Issues (Headless Servers)**  
   - Always set `matplotlib.use("Agg")` to avoid display errors on cloud/CLI environments.

2. **Memory Leaks or Plot Hangs**  
   - Use `plt.close()` after saving plots to free memory in repeated runs.

3. **Font Cache Delay**  
   - The first time matplotlib runs, it may build the font cache; this can cause a short delay.

4. **Entropy Criterion Not Found**  
   - Ensure correct scikit-learn version is installed (`pip install -U scikit-learn`).
