# Practice Q4. Find the maximum among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print("Maximum number =", maximum)

# -------Output-------
# Enter first number: 45
# Enter second number: 78
# Enter third number: 23
# Maximum number = 78
