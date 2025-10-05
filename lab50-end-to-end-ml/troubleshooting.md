# Troubleshooting - Lab 50 (End-to-End ML Workflow)

### 1. Missing Libraries
pip install scikit-learn pandas numpy seaborn matplotlib --break-system-packages

### 2. Matplotlib Display Error
import matplotlib
matplotlib.use('Agg')
