# Practice Q17. Check whether a number is a palindrome or not

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# -------Output (Palindrome)-------
# Enter a number: 121
# Palindrome Number

# -------Output (Not Palindrome)-------
# Enter a number: 123
# Not a Palindrome Number
