# Troubleshooting - Lab 19

1. **Matplotlib Font Cache Delay**  
   - On first run, matplotlib may display:  
     `Matplotlib is building the font cache; this may take a moment.`  
   - This is normal and happens only on the first execution.

2. **scikit-learn Import Error**  
   - If you see `ModuleNotFoundError: No module named 'sklearn'`, install with:  
     ```bash
     pip install scikit-learn
     ```
