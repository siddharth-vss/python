# Assignment 2 - Q4
# Perform various string operations on two strings.

str1 = "Hello"
str2 = "World"

# a) Display strings and their lengths
print("String 1:", str1)
print("String 2:", str2)
print("Length of str1:", len(str1))
print("Length of str2:", len(str2))

# b) Positive and negative indexing
print("\nstr1[0]:", str1[0])
print("str1[1]:", str1[1])
print("str1[-1]:", str1[-1])
print("str1[-2]:", str1[-2])

# c) Slicing
print("\nstr1[0:3]:", str1[0:3])
print("str1[::2]:", str1[::2])
print("str1[::-1]:", str1[::-1])

# d) Repetition and concatenation
print("\nstr1 * 2:", str1 * 2)
print("str1 + str2:", str1 + str2)

# e) Membership using in and not in
print("\n'He' in str1:", "He" in str1)
print("'He' not in str1:", "He" not in str1)
print("'xy' in str1:", "xy" in str1)
print("'xy' not in str1:", "xy" not in str1)

# f) String comparison
print("\nstr1 == str2:", str1 == str2)
print("str1 != str2:", str1 != str2)
print("str1 <  str2:", str1 < str2)
print("str1 >  str2:", str1 > str2)

# g) upper() and lower()
print("\nstr1.upper():", str1.upper())
print("str1.lower():", str1.lower())
print("str2.upper():", str2.upper())
print("str2.lower():", str2.lower())
