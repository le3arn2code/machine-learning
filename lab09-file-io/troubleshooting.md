# Troubleshooting

## Common Issues and Fixes

### 1. FileNotFoundError
- **Cause:** Trying to open a file that does not exist.
- **Fix:** Use try/except with `FileNotFoundError`.

### 2. File overwritten unexpectedly
- **Cause:** Opening file with `'w'` mode erases its contents.
- **Fix:** Use `'a'` mode for appending data.

### 3. Permission errors
- **Cause:** Attempting to write where user doesn’t have permission.
- **Fix:** Run in a directory with write access.

### 4. OSError
- **Cause:** General OS-level error like path issue.
- **Fix:** Catch with `except OSError as e` and display the error.
