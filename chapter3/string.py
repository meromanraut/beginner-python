#string is the sequence of characters enclosed in single or double quotes
name = "me.roman.raut"
name2 = 'me.roman.raut'
name3 = """me.roman.raut"""
name4 = '''me.roman.raut'''
# string can be enclosed in single quotes, double quotes, triple single quotes or triple double quotes
print(name)
print(name2)
print(name3)
print(name4)

# string can be concatenated using + operator
name5 = name + " " + name2 + " " + name3 + " " + name4
print(name5)

# string can be repeated using * operator
name6 = name * 3
print(name6)

# string can be sliced using [start:end] notation
name7 = name[0:4]  # slicing the first 4 characters
#output wil be 'me.r'
print(name7)

# string can be sliced using [start:end:step] notation
name8 = name[0:10:2]  # slicing the first 10 characters with step 2
#ouput will be 'm.rn.a'
print(name8)

# string can be sliced using [start:] notation
print("name9")
name9 = name[0:]  # slicing from the start to the end
print(name9)

# string can be sliced using [:end] notation
name10 = name[:4]  # slicing from the start to the 4th character
print(name10)


# string can be sliced using [::-1] notation to reverse the string
name11 = name[::-1]  # reversing the string
print(name11)

# string can be sliced using [start:end:step] notation to reverse the string
name12 = name[4:0:-1]  # slicing from the 4th character to the start with step -1
print(name12)  # output will be 'm.rae'
