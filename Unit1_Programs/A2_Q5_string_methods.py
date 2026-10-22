# Assignment 2 - Q5
# Perform various string methods on a sentence.

sentence = "  Hello World Python Hello  "

# a) Remove leading and trailing spaces
print("Original   :", repr(sentence))
print("lstrip()   :", repr(sentence.lstrip()))
print("rstrip()   :", repr(sentence.rstrip()))
print("strip()    :", repr(sentence.strip()))
sentence = sentence.strip()

# b) Search using find() and index()
print("\nfind('Python'):", sentence.find("Python"))
print("find('Java'):", sentence.find("Java"))
print("index('World'):", sentence.index("World"))
try:
    print("index('Java'):", sentence.index("Java"))
except ValueError:
    print("index('Java'): 'Java' not found (ValueError raised)")

# c) Count occurrences
print("\ncount('Hello'):", sentence.count("Hello"))
print("count('o'):", sentence.count("o"))

# d) Replace
print("\nreplace('Hello', 'Hi'):", sentence.replace("Hello", "Hi"))
print("replace('o', '0'):", sentence.replace("o", "0"))

# e) split() and join()
words = sentence.split()
print("\nsplit():", words)
print("join() with '-':", "-".join(words))
print("join() with ' ':", " ".join(words))

# f) Immutability demo + sort words
print("\nAttempting sentence[0] = 'X' ...")
try:
    sentence[0] = 'X'
except TypeError as e:
    print("Error:", e)
    print("Strings are immutable — characters cannot be modified via indexing.")

sorted_words = sorted(sentence.split())
print("Words sorted alphabetically:", sorted_words)
