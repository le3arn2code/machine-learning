# Interview Q&A - Lab 16 (Matplotlib Basics)

**Q1: What is Matplotlib used for?**  
A: It is a Python library for creating static, interactive, and animated plots.

**Q2: Difference between plt.plot() and plt.bar()?**  
A: `plt.plot()` is for line graphs (continuous data), while `plt.bar()` is for bar charts (categorical data).

**Q3: Why use plt.savefig() in cloud VMs?**  
A: Because they may not support GUI display (`plt.show()`), so saving ensures results are stored as images.

**Q4: How do you customize a plot?**  
A: Using functions like `plt.title()`, `plt.xlabel()`, and `plt.ylabel()`.

**Q5: What are common issues with Matplotlib in servers?**  
A: Missing dependencies, backend errors, or scripts hanging due to `plt.show()` in headless mode.
