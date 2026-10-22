# Assignment 2 - Q1
# Create a list of ten integers using range() and perform various list operations.

my_list = list(range(10, 110, 10))

# a) Display list; positive indexing, negative indexing, slicing
print("List:", my_list)
print("Positive index [0]:", my_list[0])
print("Positive index [4]:", my_list[4])
print("Negative index [-1]:", my_list[-1])
print("Negative index [-3]:", my_list[-3])
print("Slice [2:6]:", my_list[2:6])
print("Slice [::2]:", my_list[::2])

# b) Update element at index 3
my_list[3] = 99
print("\nAfter updating index 3 to 99:", my_list)

# c) Concatenation and repetition
list2 = [100, 200, 300]
print("\nConcatenation (+):", my_list + list2)
print("Repetition (*2):", [1, 2, 3] * 2)

# d) Membership using in and not in
print("\n99 in list:", 99 in my_list)
print("99 not in list:", 99 not in my_list)
print("55 in list:", 55 in my_list)
print("55 not in list:", 55 not in my_list)

# e) List methods
my_list.append(110)
print("\nAfter append(110):", my_list)
my_list.insert(0, 5)
print("After insert(0, 5):", my_list)
my_list.remove(5)
print("After remove(5):", my_list)
popped = my_list.pop()
print("After pop(), popped value:", popped)
print("List after pop():", my_list)
my_list.reverse()
print("After reverse():", my_list)
my_list.append(30)
print("After append(30):", my_list)
print("count(30):", my_list.count(30))

# f) Sorting
data = list(range(10, 110, 10))
print("\nsort() ascending:", sorted(data))
print("sorted() descending:", sorted(data, reverse=True))

# g) Alias vs Clone
original = [1, 2, 3, 4, 5]
alias = original
clone = original[:]
alias[0] = 99
clone[1] = 88
print("\nOriginal after alias[0]=99:", original)
print("Alias:", alias)
print("Clone after clone[1]=88:", clone)
print("alias is original:", alias is original)
print("clone is original:", clone is original)

# h) max, min, length
data = list(range(10, 110, 10))
print("\nList:", data)
print("Maximum:", max(data))
print("Minimum:", min(data))
print("Length:", len(data))
