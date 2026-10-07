# Practice Q10. Add some days to today's date and print the new date
# timedelta handles leap years and month-end boundaries automatically

from datetime import date, timedelta

days = int(input("Enter number of days to add: "))
today = date.today()
new_date = today + timedelta(days=days)

print("Today's date:", today)
print("Date after adding days:", new_date)

# -------Output-------
# Enter number of days to add: 10
# Today's date: 2026-10-07
# Date after adding days: 2026-10-17
