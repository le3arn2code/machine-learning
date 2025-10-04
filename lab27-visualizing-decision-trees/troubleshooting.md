# Troubleshooting Notes - Lab 27

## 1. Graphviz 'dot' not found error
If you see:
```
graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot')
```
Fix:
```
sudo apt update
sudo apt install graphviz -y
```

## 2. Permission issues while saving PDF/PNG
Ensure your working directory is writable:
```
chmod +w .
```

## 3. Headless environments
Always set:
```python
import matplotlib
matplotlib.use("Agg")
```
to avoid GUI errors on servers or cloud VMs.
