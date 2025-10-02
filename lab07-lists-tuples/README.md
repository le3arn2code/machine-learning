# Lab 7: Python Data Structures - Lists and Tuples

## Objectives
- Understand how to create and manipulate lists in Python.
- Learn how to create tuples and access elements.
- Discuss the concepts of mutability and immutability in Python data structures.

## Prerequisites
- Basic understanding of Python syntax.
- Familiarity with Python data types and variables.

---

## Tasks and Files

### Task 1: Create and Manipulate Lists
- File: `lab07_lists.py`
- Covers creating lists, adding/removing elements, and slicing.

### Task 2: Create Tuples and Access Elements
- File: `lab07_tuples.py`
- Covers tuple creation and accessing elements.

### Task 3: Mutability vs Immutability
- File: `lab07_mutability.py`
- Demonstrates list mutability and tuple immutability.

---

## Layman's Explanation
- **List** = Shopping list: you can add/remove/replace items freely.  
- **Tuple** = Birth certificate: once created, it cannot be changed.  

Lists are flexible but can change; tuples are fixed and efficient when data should remain constant.

---

## Issues Faced and Fixes

1. **Wrong filename run**  
   - Issue: Typo in filename caused `No such file` error.  
   - Fix: Double-checked names before running.  

2. **Accidentally modifying tuple**  
   - Issue: Uncommenting tuple modification raised `TypeError`.  
   - Fix: Left tuple unchanged, as expected.  

3. **Python version mismatch**  
   - Issue: Running with `python` (v2) caused syntax issues.  
   - Fix: Used `python3 filename.py`.  

---

## Conclusion
By completing this lab, you practiced:
- **Lists** → creation, adding, removing, slicing.  
- **Tuples** → creation, accessing.  
- **Mutability vs Immutability** → modifying lists vs immutable tuples.  

Lists and tuples are **core data structures**. Choosing the right one improves clarity and efficiency in Python programs.
