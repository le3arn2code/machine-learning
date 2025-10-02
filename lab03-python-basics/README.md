# Lab 3: Python Basics - Variables and Data Types

## Objectives
- Understand and declare different data types in Python: int, float, str, and bool.
- Learn how to print variable values.
- Explore type conversion between various data types.

## Prerequisites
- Basic understanding of Python syntax.
- Ability to execute Python scripts using an interpreter like Python's IDLE or an IDE like PyCharm or VSCode.

## Tasks
### Task 1: Declare Variables with Different Types
```python
age = 25
pi = 3.14159
name = "Alice"
is_student = True
```

### Task 2: Print Variable Values
```python
print("Name:", name)
print("Age:", age)
print("PI value:", pi)
print("Is student:", is_student)
```

### Task 3: Experiment with Type Conversion
```python
result = age + 5.5
print("Result:", result)

whole_number = int(pi)
print("Whole number:", whole_number)

age_str = str(age)
print("Age as a string:", age_str)
```

---

## Layman's Explanation
This lab is about learning the **very basics of Python**. Think of variables like boxes where you store information. For example:
- `age = 25` means we put the number 25 in a box called *age*.
- `pi = 3.14159` is like putting a decimal number in a box.
- `name = "Alice"` means we put the word "Alice" in a box.
- `is_student = True` means the box has a "yes/no" type answer.

We then used the `print()` function to show what’s inside each box.  
Later, we practiced **converting** these values. For example, changing a decimal into a whole number, or a number into text.  
This is important because in real life programs, data often needs to be transformed before use.

---

## Issues Faced and How We Solved Them
1. **Duplicate Output**
   - Issue: Code was run twice, so the same output repeated.  
   - Fix: Ensure the file has only one copy of the code before saving.

2. **Software Mismatch**
   - Issue: Sometimes Python commands may fail if `python` points to version 2 instead of 3.  
   - Fix: Always use `python3 filename.py` to avoid version conflicts.

3. **File Not Saved in nano**
   - Issue: Forgetting to save before running the program.  
   - Fix: In nano, press `CTRL+O` to save and `CTRL+X` to exit.

---

## Conclusion
By completing this lab, you learned how to:
- Create variables in Python.
- Print them on screen.
- Convert between different types.  
This is the **foundation of Python programming**, like learning ABC before writing sentences.
