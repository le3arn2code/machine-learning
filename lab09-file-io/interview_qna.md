# Interview Q&A

1. **Q: What does the open() function do in Python?**
   A: It opens a file and returns a file object.

2. **Q: What are the different modes for opening files?**
   A: 'r' (read), 'w' (write), 'a' (append), 'b' (binary), 'x' (exclusive creation).

3. **Q: What happens if you open a file in 'w' mode that already exists?**
   A: The file is truncated (erased) before writing new data.

4. **Q: What’s the difference between 'w' and 'a' mode?**
   A: 'w' overwrites the file, 'a' appends data at the end.

5. **Q: What is the purpose of using with open()?**
   A: It ensures the file is closed automatically after use.

6. **Q: How do you read a file line by line in Python?**
   A: By iterating over the file object in a for loop.

7. **Q: How do you handle missing files gracefully?**
   A: Use try/except and catch `FileNotFoundError`.

8. **Q: Can you write both text and binary files in Python?**
   A: Yes, with text mode ('t') or binary mode ('b').

9. **Q: What is OSError in file handling?**
   A: A general error raised for issues like permissions or invalid paths.

10. **Q: Give a real-world analogy of file modes.**
    A: 'r' = reading a book, 'w' = erasing and rewriting, 'a' = adding notes at the end.
