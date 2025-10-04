# Troubleshooting

| Issue | Cause | Solution |
|--------|--------|-----------|
| AttributeError for .days | Wrong variable type | Ensure both operands are datetime objects |
| Negative holiday days | Current date > holiday date | Use a future date for `holiday_date_string` |
| Wrong parsing format | Format mismatch | Match string format with `%Y-%m-%d` |
