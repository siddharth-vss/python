# Practice Q13. Find HCF (GCD) of two numbers using Euclidean algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("HCF / GCD =", a)

# -------Output-------
# Enter first number: 48
# Enter second number: 18
# HCF / GCD = 6
