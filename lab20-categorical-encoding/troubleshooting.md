# Troubleshooting - Lab 20

1. **Error: `TypeError: OneHotEncoder.__init__() got an unexpected keyword argument 'sparse'`**
   - Cause: scikit-learn v1.4+ changed the argument name.
   - Fix: Use `sparse_output=False` instead of `sparse=False`.

2. **No module named 'sklearn'**
   - Ensure scikit-learn is installed: `pip install scikit-learn`
