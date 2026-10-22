# Assignment 2 - Q6
# Use Python's array module to create an integer array and perform various operations.

import array

my_array = array.array('i', [15, 30, 45, 60, 75, 90, 105, 120])

# a) Display array; indexing and slicing
print("Array:", list(my_array))
print("Index [0]:", my_array[0])
print("Index [-1]:", my_array[-1])
print("Slice [2:5]:", list(my_array[2:5]))
print("Slice [::2]:", list(my_array[::2]))

# b) Insert element at position 2
my_array.insert(2, 35)
print("\nAfter insert(2, 35):", list(my_array))

# c) Remove element and pop last
my_array.remove(35)
print("\nAfter remove(35):", list(my_array))
popped = my_array.pop()
print("After pop(), removed:", popped)
print("Array after pop():", list(my_array))

# d) Search for an element
search = 60
try:
    idx = my_array.index(search)
    print("\n" + str(search), "found at index:", idx)
except ValueError:
    print("\n" + str(search), "not found in the array.")

search2 = 999
try:
    idx2 = my_array.index(search2)
    print(search2, "found at index:", idx2)
except ValueError:
    print(search2, "not found in the array.")

# e) Membership using in and not in
print("\n60 in array:", 60 in my_array)
print("60 not in array:", 60 not in my_array)
print("999 in array:", 999 in my_array)
print("999 not in array:", 999 not in my_array)

# f) max, min, length
print("\nMaximum:", max(my_array))
print("Minimum:", min(my_array))
print("Length:", len(my_array))

# g) Reverse
my_array.reverse()
print("\nAfter reverse():", list(my_array))
