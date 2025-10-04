# Interview Q&A - Lab 32

1. What is a regular expression?
   - A sequence of characters that defines a search pattern for text matching.

2. Which Python module handles regex?
   - The `re` module.

3. Difference between `re.search()` and `re.findall()`?
   - `search()` returns the first match, `findall()` returns all matches.

4. How do you remove special characters using regex?
   - `re.sub(r'[^\w\s]', '', text)`

5. What is a capturing group?
   - Parentheses `()` in regex that extract portions of the match.

6. How can you make a regex case-insensitive?
   - Use the flag `re.IGNORECASE`.

7. Explain the purpose of raw strings (r"") in regex.
   - Prevents Python from treating backslashes as escape characters.

8. What is a backreference in regex?
   - Reusing a captured group via `\1`, `\2`, etc.

9. Can regex be used for validation?
   - Yes, e.g., validating emails, passwords, or phone numbers.

10. What’s the risk of using overly complex regex?
   - Slower execution and risk of “catastrophic backtracking”.
