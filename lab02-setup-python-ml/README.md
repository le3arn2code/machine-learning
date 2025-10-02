# Lab 02: Setting Up Python for ML

## Overview
This lab walks you through installing Python 3.x, setting up a virtual environment, and installing essential Machine Learning (ML) libraries such as NumPy, Pandas, and scikit-learn. Using a virtual environment ensures that dependencies are isolated and avoids version conflicts.

By the end of this lab, you will have a functioning ML development environment on Ubuntu 24, with verified installations of the core libraries. This sets the foundation for building ML models in later labs.

## Lab Goals
- Install and verify Python 3.x on Ubuntu 24.
- Set up and activate a virtual environment using `venv`.
- Install and validate NumPy, Pandas, and scikit-learn.

## Steps Performed
1. Updated apt cache (`sudo apt update`) without running a full upgrade (break method).
2. Installed Python 3.x and pip using `sudo apt install -y python3 python3-pip`.
3. Verified installation with `python3 --version` and `pip3 --version`.
4. Installed the `venv` module using `sudo apt install -y python3-venv`.
5. Created project folder `~/ml-lab02` and moved inside it.
6. Created virtual environment using `python3 -m venv myenv`.
7. Activated environment with `source myenv/bin/activate`.
8. Installed libraries: `pip install numpy pandas scikit-learn`.
9. Verified by importing libraries in Python REPL and printing versions.

## Final Outcome
- Python 3.12.3 installed successfully.
- Virtual environment (`myenv`) created and activated.
- Libraries installed with the following versions:
  - NumPy: 2.3.3
  - Pandas: 2.3.3
  - Scikit-learn: 1.7.2
- Verified imports produced no errors.

## Errors and Resolutions
- Issue: Some systems use `python3` instead of `python`.  
  Resolution: Used `python3` consistently for Ubuntu.  
- Issue: Pip may be missing in some minimal installs.  
  Resolution: Installed via `sudo apt install python3-pip`.  
- Issue: Virtual environment activation differs by OS.  
  Resolution: For Ubuntu, used `source myenv/bin/activate`.  

## Software Stack
- Ubuntu 24.04 LTS
- Python 3.12.3
- pip (24.x)
- virtualenv/venv module
- NumPy 2.3.3
- Pandas 2.3.3
- Scikit-learn 1.7.2
