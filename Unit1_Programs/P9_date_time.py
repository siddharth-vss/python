# Practice Q9. Print today's date and current time using datetime module

from datetime import datetime

now = datetime.now()

print("Today's Date:", now.date())
print("Current Time:", now.time())
print("Date and Time:", now)

# -------Output-------
# Today's Date: 2026-10-07
# Current Time: 22:18:45.123456
# Date and Time: 2026-10-07 22:18:45.123456
