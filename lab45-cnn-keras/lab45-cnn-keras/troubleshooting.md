# Troubleshooting Guide

## Common Issues

### 1. TensorFlow CUDA Error
If running on a VM without GPU support:
```
export CUDA_VISIBLE_DEVICES=""
```
This disables GPU usage safely.

### 2. No Display Error
This lab uses **matplotlib in headless mode** (`matplotlib.use('Agg')`), so plots are saved, not displayed.

### 3. Memory Issues
Close figures after saving to free memory in limited environments.
