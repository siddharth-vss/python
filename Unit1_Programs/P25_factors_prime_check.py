# Practice Q25. Find factors of N using a function, then check if N is prime

def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

num = int(input("Enter a number: "))
f = factors(num)

print("Factors:", f)

if len(f) == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# -------Output (Prime)-------
# Enter a number: 7
# Factors: [1, 7]
# Prime Number

# -------Output (Not Prime)-------
# Enter a number: 12
# Factors: [1, 2, 3, 4, 6, 12]
# Not a Prime Number
