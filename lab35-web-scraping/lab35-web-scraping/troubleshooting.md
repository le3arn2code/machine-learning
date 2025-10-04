# Troubleshooting for Lab 35

- **Error: ModuleNotFoundError**
  Install missing packages:
  ```bash
  pip install beautifulsoup4 requests
  ```

- **Error: ConnectionError**
  Ensure your VM has internet access.

- **Empty output**
  The target site might have changed structure. Use `print(soup.prettify())` to debug.
