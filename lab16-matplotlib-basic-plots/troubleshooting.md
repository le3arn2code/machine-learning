# Troubleshooting - Lab 16

## Issue 1: Matplotlib not installed
**Error:**
```
ModuleNotFoundError: No module named 'matplotlib'
```
**Solution:**
Install matplotlib:
```
pip install matplotlib --break-system-packages
```

## Issue 2: Script hangs on cloud VM
- Cause: Using `plt.show()` in headless/CLI environment.
- Fix: Use `plt.savefig()` instead of `plt.show()`.

## Issue 3: Old PNG not updating
- Reason: File already exists.
- Fix: Overwrite with new run (`plt.savefig(...)` automatically replaces).
