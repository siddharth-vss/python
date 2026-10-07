# Practice Q5. Keep accepting numbers until user enters 0, then print the sum

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total = total + num

print("Sum =", total)

# -------Output-------
# Enter a number (0 to stop): 10
# Enter a number (0 to stop): 20
# Enter a number (0 to stop): 30
# Enter a number (0 to stop): 0
# Sum = 60
