# Troubleshooting

## Common Issues and Fixes

### 1. KeyError on dictionary access
- **Cause:** Accessing a non-existing key.
- **Fix:** Use `get()` method with default value, e.g., `book.get("publisher", "N/A")`.

### 2. KeyError on set remove()
- **Cause:** Using `remove()` for non-existing element.
- **Fix:** Use `discard()` for safe removal.

### 3. Duplicates in sets
- **Cause:** Trying to insert duplicate values.
- **Fix:** Remember sets automatically ignore duplicates.

### 4. Python version mismatch
- **Cause:** Running with `python` (v2).
- **Fix:** Use `python3 filename.py`.
