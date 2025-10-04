# Troubleshooting Guide

**1. Matplotlib display issues**
- Always use headless mode (`matplotlib.use('Agg')`) on cloud VMs.

**2. Memory or hanging issues**
- Always call `plt.close()` after saving figures.

**3. Import Errors**
- Ensure all required libraries are installed using pip.
