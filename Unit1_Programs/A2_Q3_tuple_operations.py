# Assignment 2 - Q3
# Tuple with at least ten values including repeated numeric values.

my_tuple = (10, 25, 30, 25, 50, 60, 25, 80, 90, 100)
print("Tuple:", my_tuple)

# a) Positive indexing, negative indexing, slicing
print("\nPositive index [0]:", my_tuple[0])
print("Positive index [3]:", my_tuple[3])
print("Negative index [-1]:", my_tuple[-1])
print("Negative index [-2]:", my_tuple[-2])
print("Slice [1:5]:", my_tuple[1:5])
print("Slice [::3]:", my_tuple[::3])

# b) Concatenation and repetition
extra = (110, 120)
print("\nConcatenation (+):", my_tuple + extra)
print("Repetition (*2) on (1,2,3):", (1, 2, 3) * 2)

# c) Membership using in and not in
print("\n25 in tuple:", 25 in my_tuple)
print("25 not in tuple:", 25 not in my_tuple)
print("99 in tuple:", 99 in my_tuple)
print("99 not in tuple:", 99 not in my_tuple)

# d) max, min, length
print("\nMaximum:", max(my_tuple))
print("Minimum:", min(my_tuple))
print("Length:", len(my_tuple))

# e) Count occurrences
print("\nCount of 25:", my_tuple.count(25))
print("Count of 10:", my_tuple.count(10))

# f) Search using index()
print("\nIndex of 50:", my_tuple.index(50))
try:
    print("Index of 99:", my_tuple.index(99))
except ValueError:
    print("99 not found in the tuple.")
