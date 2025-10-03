# Troubleshooting

- **Matplotlib font cache delay**: The first run may take longer due to font cache building.
- **Headless mode**: Ensure `matplotlib.use('Agg')` is set on cloud VMs with no display.
- **Close plots**: Always use `plt.close()` after saving to avoid memory issues.
