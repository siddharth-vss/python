# Practice Q11. Print the sum of the series 1/2 + 1/3 + 1/4 + ... + 1/N

n = int(input("Enter N: "))
total = 0

for i in range(2, n + 1):
    total = total + (1 / i)

print("Sum of series =", total)

# -------Output-------
# Enter N: 5
# Sum of series = 1.2833333333333332
