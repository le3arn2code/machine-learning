# Lab 6: Python Basics - Loops and Iterations

## Objectives
- Understand the concept of loops and iterations in Python.
- Practice using for and while loops effectively.
- Execute and control iterations with practical examples.
- Develop skills to print outputs during iterations.

## Prerequisites
- Basic understanding of Python syntax.
- Familiarity with Python lists and basic data types.
- Python installed on your system or access to an online compiler.

---

## Tasks and Files

### Task 1: For Loop over a List
- File: `lab06_for_loop_list.py`
- Iterates through a list of numbers and prints each.

### Task 2: While Loop with Counter
- File: `lab06_while_loop.py`
- Uses a while loop to print numbers until count reaches 5.

### Task 3: Iteration Tracking
- File: `lab06_iteration_tracking.py`
- Demonstrates enhanced for and while loops with iteration start and end markers.

---

## Layman's Explanation
Loops are like **repeating instructions**.  
Example: "Say hello to 5 people, one after another." Instead of writing 5 lines, you write one loop that repeats.  

- **for loop** → repeats for each item in a collection (like a list of numbers).  
- **while loop** → repeats until a condition is no longer true (like count reaching 5).  
- **iteration tracking** → helps see what happens at the start and end of each cycle, useful for debugging.

---

## Issues Faced and Fixes

1. **Typo in filenames**  
   - Issue: Running wrong filename gave "No such file or directory".  
   - Fix: Ensure filenames match exactly (`lab06_for_loop_list.py`).  

2. **Infinite loop risk**  
   - Issue: Forgetting `count += 1` in while loop causes infinite repetition.  
   - Fix: Always increment counters inside while loops.  

3. **Python version mismatch**  
   - Issue: Running `python` defaulted to Python 2.  
   - Fix: Always use `python3 filename.py`.  

---

## Conclusion
By completing this lab, you learned:
- Iterating through lists with **for loops**.  
- Repeating tasks under a condition with **while loops**.  
- Tracking start and end of iterations for debugging.  

Loops are essential for automating tasks and handling large datasets in real programs.
