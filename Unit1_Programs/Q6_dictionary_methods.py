# Q6. Create a dictionary and apply: print items, access items, get(), change values, len()

# Create a dictionary
student = {
    "name": "Rahul",
    "course": "MCA",
    "semester": 3,
    "marks": 85
}

# 1. Print the dictionary items
print("Dictionary:", student)

# 2. Access items
print("Student Name:", student["name"])
print("Course:", student["course"])

# 3. Use get()
print("Semester:", student.get("semester"))
print("Marks:", student.get("marks"))

# 4. Change values
student["marks"] = 90
student["semester"] = 4
print("Dictionary after changing values:", student)

# 5. Use len()
print("Number of items:", len(student))

# -------Output-------
# Dictionary: {'name': 'Rahul', 'course': 'MCA', 'semester': 3, 'marks': 85}
# Student Name: Rahul
# Course: MCA
# Semester: 3
# Marks: 85
# Dictionary after changing values: {'name': 'Rahul', 'course': 'MCA', 'semester': 4, 'marks': 90}
# Number of items: 4
