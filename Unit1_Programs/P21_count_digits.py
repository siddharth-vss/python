# Practice Q21. Count number of digits in a number using a function

def count_digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count

num = int(input("Enter a number: "))
result = count_digits(num)
print("Number of digits =", result)

# -------Output-------
# Enter a number: 98765
# Number of digits = 5
