# Practice Q18. Count frequency of characters in a string and store in a dictionary

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("Character frequency:")
print(frequency)

# -------Output-------
# Enter a string: hello
# Character frequency:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
