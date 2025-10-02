# Interview Q&A - Lab 10 (NumPy Arrays)

**Q1: What is NumPy and why is it used?**  
A: NumPy is a Python library for numerical computing. It provides efficient arrays and mathematical operations, crucial for data science and ML.

**Q2: How are NumPy arrays different from Python lists?**  
A: Lists can store mixed data types and are slower for large computations. NumPy arrays are homogeneous, memory-efficient, and support vectorized operations.

**Q3: What is broadcasting in NumPy?**  
A: Broadcasting allows NumPy to perform arithmetic on arrays of different shapes by automatically expanding dimensions.

**Q4: How do you create a 1D and 2D array in NumPy?**  
A: Using `np.array([..])` for 1D and `np.array([[..],[..]])` for 2D arrays.

**Q5: What happens if you try to add two Python lists vs NumPy arrays?**  
A: Lists concatenate, but NumPy arrays add element-wise.

**Q6: What is slicing in NumPy?**  
A: Extracting a subset of array elements using index ranges, e.g. `arr[1:4]`.

**Q7: Can you explain the difference between shallow copy and deep copy in NumPy?**  
A: Shallow copies (views) share data buffer; deep copies allocate new memory. Example: `arr.copy()` makes a deep copy.

**Q8: How to check the shape and dimension of an array?**  
A: Use `.shape` for shape (rows, cols) and `.ndim` for dimensions.

**Q9: Why is NumPy faster than lists?**  
A: NumPy arrays use contiguous memory blocks and are implemented in C, enabling vectorized operations without Python loops.

**Q10: Give a real-world use case of NumPy arrays.**  
A: Data preprocessing in ML, image manipulation (as arrays of pixels), or large-scale numerical simulations.

