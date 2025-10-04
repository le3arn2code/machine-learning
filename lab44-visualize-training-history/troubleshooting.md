# Troubleshooting

1. **CUDA Error**
   - If you see: `INTERNAL: CUDA error`, your system lacks GPU support.
   - Fix: Run CPU-only training; TensorFlow handles this automatically.

2. **Blank Plots**
   - Ensure Matplotlib is installed and the backend supports rendering.
   - Run: `pip install matplotlib`

3. **Slow Training**
   - Reduce epochs (e.g., 50) for faster execution.
