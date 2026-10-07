# Q5. Create a tuple and perform: Add items, Check item, len(), Access items()

# Create a tuple
languages = ("C++", "Java", "PHP")

# Add item in tuple
languages = ("React",) + languages + ("Java",)
print("After adding elements to tuple :", languages)

# Check if item is available in tuple
if "React" in languages:
    print("React is in the tuple")
else:
    print("React is not in the language tuple")

# Check the length of the tuple
print("Length of the tuple :", len(languages))

# Access the elements of the tuple
print("First item of the tuple :", languages[0])
print("Second item of the tuple :", languages[1])
print("Last item of the tuple :", languages[-1])

# -------Output-------
# After adding elements to tuple : ('React', 'C++', 'Java', 'PHP', 'Java')
# React is in the tuple
# Length of the tuple : 5
# First item of the tuple : React
# Second item of the tuple : C++
# Last item of the tuple : Java
