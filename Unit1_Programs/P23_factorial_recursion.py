# Practice Q23. Find factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# -------Output-------
# Enter a number: 5
# Factorial = 120
