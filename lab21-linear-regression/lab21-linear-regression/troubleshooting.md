# Troubleshooting Notes - Lab 21

- **Matplotlib font cache delay:**  
  The first run displayed `Matplotlib is building the font cache; this may take a moment.`  
  This is normal and only occurs the first time.

- **Headless Mode on Cloud VM:**  
  Used `matplotlib.use('Agg')` to avoid GUI issues and save plots instead of displaying them.

- **Memory buildup/hanging:**  
  Used `plt.close()` after saving plots to prevent resource leaks in CLI/cloud environments.
