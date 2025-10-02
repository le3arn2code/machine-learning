# Lab 5: Python Basics - Functions

## Objectives
- Understand the concept of functions in Python.
- Learn to define functions with parameters.
- Learn to return values from functions.
- Practice calling functions with different arguments.

## Prerequisites
- Basic understanding of Python syntax.
- Familiarity with variables and data types in Python.

---

## Tasks and Files

### Task 1: Define a Function with Parameters
- File: `lab05_greet.py`
- Defines a simple function `greet(name)` that prints a message.

### Task 2: Return a Value from the Function
- File: `lab05_square.py`
- Defines a function `square(number)` that returns the square of a number.

### Task 3: Call Functions with Different Arguments
- File: `lab05_calls.py`
- Calls both `greet()` and `square()` with different inputs.

---

## Layman's Explanation
Think of a **function** like a small machine. You give it an input, it does its job, and (sometimes) gives you an output.  

Examples from this lab:
- `greet("Alice")` → Machine prints: *Hello, Alice!*  
- `square(5)` → Machine calculates and gives you: *25*  

This makes programs modular and reusable, just like reusing the same machine for different tasks.

---

## Issues Faced and Fixes

1. **Forgot to save file in nano**  
   - Issue: Running gave `No such file` error.  
   - Fix: Use `CTRL+O` to save, `CTRL+X` to exit.  

2. **Python version mismatch**  
   - Issue: `python` ran Python 2 (caused syntax errors).  
   - Fix: Always run with `python3`.  

3. **Function not returning value**  
   - Issue: Initially only printed values without `return`.  
   - Fix: Added `return` for `square()` so results can be stored and reused.  

---

## Conclusion
By completing this lab, you practiced:
- Defining functions with parameters.
- Returning values with `return`.
- Reusing functions with different arguments.  

Functions make code more **organized, modular, and reusable**, which is key in real-world programming.
