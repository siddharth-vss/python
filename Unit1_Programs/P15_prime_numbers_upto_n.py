# Practice Q15. Print all prime numbers up to N (N > 100)

n = int(input("Enter N: "))
print("Prime numbers:")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# -------Output (N=50)-------
# Enter N: 50
# Prime numbers:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
