# Troubleshooting

| Issue | Cause | Solution |
|--------|--------|-----------|
| `ModuleNotFoundError: No module named 'keras'` | Keras/TensorFlow not installed | Run: `pip install tensorflow keras` |
| GPU-related CUDA error | TensorFlow GPU setup issue | Use CPU backend by uninstalling GPU version |
| Accuracy fluctuates too much | Random dataset used | Expected; use real data for stable accuracy |
| Training slow | Limited CPU resources | Reduce epochs or batch size |
