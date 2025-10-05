# Troubleshooting - Lab 46

## ⚠️ Common Warnings

### 1. CUDA Driver Warning
```
did not find cuda drivers on your machine, GPU will not be used
```
**Cause:** TensorFlow is optimized for GPU but runs fine on CPU.
**Fix:** Ignore this warning in CPU-only environments.

### 2. Input Shape Deprecation
```
Do not pass an `input_shape` argument to Sequential models...
```
**Cause:** Keras suggests using `Input(shape=...)` for new versions.
**Fix:** Safe to ignore; current syntax still works.

## ✅ Outcome
Your model trained successfully with loss ≈ 269 and predictions increasing smoothly.
