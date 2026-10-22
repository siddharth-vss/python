# Assignment 2 - Q2
# Student name list and nested list with names and marks.

# list1 - names of five students
list1 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# list2 - nested list: [name, marks]
list2 = [
    ["Alice", 85],
    ["Bob", 72],
    ["Charlie", 91],
    ["Diana", 68],
    ["Eve", 78]
]

print("Student Names (list1):", list1)
print("Student Records (list2):", list2)

# a) Search for a student name in list1
name = "Charlie"
print("\nSearching for:", name)
if name in list1:
    print(name, "found at index:", list1.index(name))
else:
    print(name, "not found in the list.")

# b) Sort student names
list1.sort()
print("\nAscending order:", list1)
list1.sort(reverse=True)
print("Descending order:", list1)

# c) Add, insert, and remove
list1.append("Frank")
print("\nAfter append('Frank'):", list1)
list1.insert(2, "Grace")
print("After insert(2, 'Grace'):", list1)
list1.remove("Grace")
print("After remove('Grace'):", list1)

# d) Display all student records using a loop
print("\nAll Student Records:")
print(f"{'Name':<12} {'Marks'}")
print("-" * 20)
for record in list2:
    print(f"{record[0]:<12} {record[1]}")

# e) Highest marks and average marks
highest = max(list2, key=lambda x: x[1])
average = sum(record[1] for record in list2) / len(list2)
print("\nStudent with highest marks:", highest[0], "->", highest[1])
print("Average marks: {:.2f}".format(average))

# f) Number of student records
print("\nTotal student records:", len(list2))
