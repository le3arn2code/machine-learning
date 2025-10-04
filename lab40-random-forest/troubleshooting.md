
# Troubleshooting Guide

1. **ModuleNotFoundError: No module named 'sklearn'**
   - Run: `pip install scikit-learn pandas numpy seaborn matplotlib`

2. **Empty plot**
   - Ensure `plt.show()` or `plt.savefig()` is correctly used (headless mode uses save).

3. **Accuracy too low**
   - Verify dataset split and random state consistency.
