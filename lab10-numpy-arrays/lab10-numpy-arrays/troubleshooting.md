# Troubleshooting - Lab 10 NumPy Arrays

## Error: ModuleNotFoundError: No module named 'numpy'
**Cause:** NumPy was not installed.  
**Fix:** Run:
```bash
pip3 install numpy --break-system-packages
```

## Error: Wrong slicing results
**Cause:** Incorrect slice indices used.  
**Fix:** Double-check ranges, remembering Python uses 0-based indexing and the end index is exclusive.

