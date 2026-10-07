# Practice Q22. Find sum of 1^5 + 2^5 + ... + N^5

n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + (i ** 5)

print("Sum of 1^5 + 2^5 + ... + {}^5 = {}".format(n, total))

# -------Output-------
# Enter N: 3
# Sum of 1^5 + 2^5 + ... + 3^5 = 276
