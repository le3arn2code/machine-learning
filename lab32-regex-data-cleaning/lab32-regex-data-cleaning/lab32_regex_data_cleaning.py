"""
Lab 32 - Using Regular Expressions for Data Cleaning
"""

import re

# ---------------- Task 1: Write Regex Patterns ----------------
print("\n--- Task 1: Simple Pattern Matching ---")
text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print(f"Matched text: {match.group()}")
else:
    print("No match found.")

# ---------------- Task 2: Find All Emails ----------------
print("\n--- Task 2: Find All Emails ---")
text = "Contact us at info@example.com or support@example.org."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print(f"Found emails: {emails}")

# ---------------- Task 3: Clean Text and Normalize Numbers ----------------
print("\n--- Task 3.1: Remove Punctuation ---")
text = "Hello! This, is a sample text. It's meant for cleaning."
pattern = r"[^\w\s]"
cleaned_text = re.sub(pattern, "", text)
print(f"Cleaned text: {cleaned_text}")

print("\n--- Task 3.2: Normalize Phone Numbers ---")
numbers = ["1234567890", "123-456-7890", "(123) 456-7890"]
standardized_format = []
pattern = r"(\d{3})[ -]?(\d{3})[ -]?(\d{4})"

for number in numbers:
    standardized_format.append(re.sub(pattern, r"\1-\2-\3", number))

print("Standardized phone numbers:")
for num in standardized_format:
    print(num)
