# Practice Q7. Check whether a number is an Armstrong number or not
# Armstrong: 153 = 1^3 + 5^3 + 3^3 = 153 (where 3 is the number of digits)

num = int(input("Enter a number: "))
temp = num
length = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** length
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# -------Output (Armstrong)-------
# Enter a number: 153
# Armstrong Number

# -------Output (Not Armstrong)-------
# Enter a number: 100
# Not an Armstrong Number
