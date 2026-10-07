# Q3. Calculate Employee Bonus based on years of service
# Less than 2 years: 5%, 2-5 years: 10%, 6-10 years: 15%, >10 years: 20%

basic_salary = float(input("Enter basic salary: "))
years = int(input("Enter years of service: "))

if years < 2:
    bonus = basic_salary * 5 / 100
elif years <= 5:
    bonus = basic_salary * 10 / 100
elif years <= 10:
    bonus = basic_salary * 15 / 100
else:
    bonus = basic_salary * 20 / 100

gross_salary = basic_salary + bonus

print("Basic Salary =", basic_salary)
print("Bonus =", bonus)
print("Gross Salary =", gross_salary)

# -------Output-------
# Enter basic salary: 50000
# Enter years of service: 7
# Basic Salary = 50000.0
# Bonus = 7500.0
# Gross Salary = 57500.0
