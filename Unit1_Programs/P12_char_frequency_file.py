# Practice Q12. Count frequency of characters in a given file

# Create a sample file for demonstration
with open("sample.txt", "w") as f:
    f.write("Hello World Python Programming")

file = open("sample.txt", "r")
text = file.read()
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

file.close()

print("Character Frequency:")
for char, count in frequency.items():
    print(char, ":", count)

# -------Output-------
# Character Frequency:
# H : 1
# e : 1
# l : 3
# o : 3
#   : 3
# W : 1
# r : 2
# d : 1
# P : 1
# y : 1
# t : 1
# h : 1
# n : 2
# g : 2
# a : 1
# m : 2
# i : 1
