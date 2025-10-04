#!/usr/bin/env python3
import datetime

print("\n--- Task 1: Parse Dates with the datetime Module ---")
date_string = "2023-10-03"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

print("\n--- Task 2: Extract Components (Day, Month, Year) ---")
print("Year:", parsed_date.year)
print("Month:", parsed_date.month)
print("Day:", parsed_date.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

print("\n--- Task 3: Compute Time Differences ---")
another_date_string = "2023-10-10"
another_date = datetime.datetime.strptime(another_date_string, "%Y-%m-%d")
date_difference = another_date - parsed_date
print("Difference in Days:", date_difference.days)

holiday_date_string = "2023-12-25"
holiday_date = datetime.datetime.strptime(holiday_date_string, "%Y-%m-%d")
days_until_holiday = holiday_date - current_datetime
print("Days until holiday:", days_until_holiday.days)

print("\n--- Lab 34 Completed Successfully ---")
print("You have practiced parsing, extracting, and computing with datetime objects.")
