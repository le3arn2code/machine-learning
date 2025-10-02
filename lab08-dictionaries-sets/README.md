# Lab 8: Python Data Structures - Dictionaries and Sets

## Objectives
- Learn to create and manage dictionaries in Python.
- Understand the functionality of sets and perform operations on them.
- Explore practical use-cases for dictionaries and sets.

## Prerequisites
- Basic understanding of Python programming.
- Familiarity with data types like integers, strings, and lists.

---

## Tasks and Files

### Task 1: Create a Dictionary
- File: `lab08_dictionary.py`
- Create a dictionary with key-value pairs (student, book).

### Task 2: Update and Access Dictionary Values
- File: `lab08_dictionary_update.py`
- Access values, update values, and add new key-value pairs.

### Task 3: Create and Manipulate Sets
- File: `lab08_sets.py`
- Create sets, add/remove elements, perform union and intersection.

---

## Layman's Explanation
- **Dictionary**: Like a real dictionary with words (keys) and definitions (values). You look up by key to get its value.  
- **Set**: Like a basket of unique fruits — no duplicates allowed. Useful for removing duplicates and doing "math-like" operations (union, intersection).  

---

## Issues Faced and Fixes

1. **KeyError when removing from set**
   - Cause: Using `remove()` for an item that didn’t exist.
   - Fix: Use `discard()` instead, which avoids errors.

2. **KeyError accessing dictionary**
   - Cause: Accessing a non-existing key.
   - Fix: Use `dict.get(key)` with a default value.

3. **Python version mismatch**
   - Issue: Running `python` defaulted to Python 2.
   - Fix: Always run with `python3 filename.py`.

---

## Conclusion
In this lab, you learned:
- How to store and update structured information with dictionaries.
- How to maintain collections of unique items with sets.
- Practical operations like union and intersection for comparing groups.

Dictionaries and sets are efficient, widely-used structures in Python programming.
