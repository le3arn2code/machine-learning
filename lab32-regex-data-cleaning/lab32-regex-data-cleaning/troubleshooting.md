# Troubleshooting - Lab 32

## 1. No Output or Empty List
- Ensure your regex patterns use a raw string (`r"pattern"`).

## 2. re.error: unknown extension
- Double-check escape sequences. Use single backslashes inside raw strings.

## 3. Invalid Phone Number Normalization
- Make sure numbers contain 10 digits.
- Adjust regex pattern if phone format differs.

## 4. Encoding Issues
- Save files in UTF-8 encoding using `nano` or `VS Code`.
