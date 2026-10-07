# Practice Q16. Find the sum of all odd numbers between 1 to N

n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1, 2):
    total = total + i

print("Sum of odd numbers =", total)

# -------Output-------
# Enter N: 10
# Sum of odd numbers = 25
