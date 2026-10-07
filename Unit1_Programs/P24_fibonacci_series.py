# Practice Q24. Print Fibonacci series up to N terms

n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# -------Output-------
# Enter number of terms: 8
# Fibonacci Series:
# 0 1 1 2 3 5 8 13
