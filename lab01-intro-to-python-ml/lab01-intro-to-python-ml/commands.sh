# Commands used in Lab 01

# Verify Python installation
python3 --version

# Install libraries
pip install numpy pandas scikit-learn

# Verify library versions inside Python
python3
>>> import numpy as np
>>> import pandas as pd
>>> import sklearn
>>> print(np.__version__)
>>> print(pd.__version__)
>>> print(sklearn.__version__)
>>> exit()

# Create script file
nano hello_ml.py
# Inside nano, add:
print("Hello, ML")
# Save (CTRL+O, ENTER) and exit (CTRL+X)

# Run the script
python3 hello_ml.py
