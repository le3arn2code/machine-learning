# Interview Q&A - Lab 02

**Q1. Why do we use virtual environments in Python?**  
A1. To isolate dependencies and prevent conflicts between projects.

**Q2. What command creates a virtual environment in Python 3?**  
A2. `python3 -m venv myenv`

**Q3. How do you activate a virtual environment on Linux/macOS?**  
A3. `source myenv/bin/activate`

**Q4. What is pip used for?**  
A4. Pip is the package manager for Python used to install libraries.

**Q5. Which libraries are essential for ML beginners?**  
A5. NumPy, Pandas, and scikit-learn.

**Q6. How do you verify that libraries are installed correctly?**  
A6. Import them in Python and check their `__version__` attributes.

**Q7. Why do we avoid running `apt upgrade` here?**  
A7. To minimize changes and avoid upgrading unrelated packages (break method).

**Q8. What is the difference between `python` and `python3` commands?**  
A8. On Ubuntu, `python` may point to Python 2 or not exist; `python3` ensures Python 3.x is used.

**Q9. What does scikit-learn provide?**  
A9. A wide range of ML algorithms and tools for data preprocessing and evaluation.

**Q10. What should you do if pip cannot install a package due to version conflicts?**  
A10. Upgrade pip, check Python version compatibility, or use a virtual environment to resolve conflicts.
