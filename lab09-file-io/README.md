# Lab 9: File I/O in Python for Data

## Objectives
- Understand the concept of File Input/Output (I/O) in Python.
- Learn how to read data from a text file.
- Learn how to write data to a file.
- Handle file exceptions using try/except.

## Prerequisites
- Basic understanding of Python programming.
- Python 3.x installed on your system.
- A text editor or IDE like VSCode, PyCharm, or Jupyter Notebook.

---

## Tasks and Files

### Task 1: Reading a File
- File: `lab09_read_file.py`
- Create a `sample.txt` file and read its content (full + line by line).

### Task 2: Writing and Appending a File
- File: `lab09_write_file.py`
- Demonstrates writing to a new file and appending to it.

### Task 3: Handling Exceptions
- File: `lab09_exceptions.py`
- Demonstrates catching `FileNotFoundError` and `OSError`.

---

## Layman's Explanation
Think of a **file** as a notebook.  
- **Reading** = opening the notebook and seeing what's inside.  
- **Writing** = erasing everything and writing new content.  
- **Appending** = adding more notes at the end.  
- **Exceptions** = handling cases when the notebook doesn’t exist or something goes wrong.

---

## Issues Faced and Fixes

1. **FileNotFoundError**  
   - Issue: Trying to open a file that does not exist.  
   - Fix: Used `try/except` to catch and handle it gracefully.  

2. **Overwriting data**  
   - Issue: Writing with `'w'` mode erased previous data.  
   - Fix: Used `'a'` mode for appending.  

3. **OS error**  
   - Issue: Permission issues or path errors.  
   - Fix: Added `except OSError` to capture and display the error message.  

---

## Conclusion
In this lab, you learned:  
- How to read files completely and line by line.  
- How to write and append data to files.  
- How to handle errors safely when files are missing or inaccessible.  

These operations are essential for working with data in Python applications.
