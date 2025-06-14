#Tuples in python
# Tuples are immutable sequences in Python, 
# used to store multiple items in a single variable.  

# They are defined by enclosing the items in parentheses"()" , separated by commas.
# Tuples can contain mixed data types, including numbers", strings, and other tuples.
# Unlike lists, tuples cannot be changed after creation, meaning 
# you cannot add, remove, or modify items.

a = (1, 2, 3, 4, 5)
b = ("apple", "banana", "cherry")
c = (1, "apple", 3.5, True)
d = ()  # empty tuple

print(a)  
print(b)  
print(c)  
print(d) 

# Accessing tuple items
print(a[0])  # 1
print(b[1])  # banana
print(c[2])  # 3.5
print(d)  # empty tuple

#slicing tuples
print(a[1:4])  # (2, 3, 4)
print(b[:2])  # ('apple', 'banana')
print(c[1:])  # ('apple', 3.5, True)

# Tuple length
print(len(a))  # 5
print(len(b))  # 3
print(len(c))  # 4
print(len(d))  # 0

# Concatenating tuples
e = a + b  # combines tuples a and b
print(e)  # (1, 2, 3, 4, 5, 'apple', 'banana', 'cherry')

# Repeating tuples
f = c * 2  # repeats tuple c twice
print(f)  # (1, 'apple', 3.5, True, 1, 'apple', 3.5, True)

# Checking if an item exists in a tuple
print(3 in a)  # True
print("banana" in b)  # True
print(4.5 in c)  # False

