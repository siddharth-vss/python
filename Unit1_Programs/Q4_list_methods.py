# Q4. Create a list and perform: insert(), remove(), append(), len(), pop(), delete()

# Create a list of computer languages
languages = ["Python", "Java", "C++", "JavaScript"]
print("Original List:", languages)

# 1. insert()
languages.insert(1, "C")
print("After insert():", languages)

# 2. remove()
languages.remove("C++")
print("After remove():", languages)

# 3. append()
languages.append("PHP")
print("After append():", languages)

# 4. len()
print("Length of list:", len(languages))

# 5. pop()
languages.pop()
print("After pop():", languages)

# 6. delete using del
del languages[1]
print("After delete (del):", languages)

# -------Output-------
# Original List: ['Python', 'Java', 'C++', 'JavaScript']
# After insert(): ['Python', 'C', 'Java', 'C++', 'JavaScript']
# After remove(): ['Python', 'C', 'Java', 'JavaScript']
# After append(): ['Python', 'C', 'Java', 'JavaScript', 'PHP']
# Length of list: 5
# After pop(): ['Python', 'C', 'Java', 'JavaScript']
# After delete (del): ['Python', 'Java', 'JavaScript']
