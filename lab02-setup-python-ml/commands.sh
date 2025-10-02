# Commands used in Lab 02 (Ubuntu 24, Break Method)

# Step 1: Update apt cache only (break method, no full upgrade)
sudo apt update

# Step 2: Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Step 3: Verify installation
python3 --version
pip3 --version

# Step 4: Install venv module
sudo apt install -y python3-venv

# Step 5: Create project directory and move inside it
mkdir ~/ml-lab02
cd ~/ml-lab02

# Step 6: Create virtual environment
python3 -m venv myenv

# Step 7: Activate virtual environment
source myenv/bin/activate

# Step 8: Install ML libraries
pip install numpy
pip install pandas
pip install scikit-learn

# Step 9: Verify in Python
python3
>>> import numpy
>>> import pandas
>>> import sklearn
>>> print("NumPy:", numpy.__version__)
>>> print("Pandas:", pandas.__version__)
>>> print("Scikit-learn:", sklearn.__version__)
>>> exit()
