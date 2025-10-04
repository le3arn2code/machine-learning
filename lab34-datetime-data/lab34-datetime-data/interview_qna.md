# Interview Q&A

**Q1:** How do you parse a date string in Python?  
**A:** Using `datetime.datetime.strptime(date_string, "%Y-%m-%d")`.

**Q2:** How do you get the current date and time?  
**A:** With `datetime.datetime.now()`.

**Q3:** What’s the difference between `datetime` and `timedelta`?  
**A:** `datetime` = point in time, `timedelta` = duration.

**Q4:** How to calculate days between two dates?  
**A:** Subtract one datetime from another, then use `.days`.

**Q5:** Real-world application?  
**A:** Event countdowns, reminders, logs, or time-based alerts.
