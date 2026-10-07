# Practice Q8. Check whether a number is a Perfect number or not
# Perfect number: sum of its factors (excluding itself) equals the number
# Example: 6 = 1 + 2 + 3

num = int(input("Enter a number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total = total + i

if total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# -------Output (Perfect)-------
# Enter a number: 6
# Perfect Number

# -------Output (Not Perfect)-------
# Enter a number: 10
# Not a Perfect Number
