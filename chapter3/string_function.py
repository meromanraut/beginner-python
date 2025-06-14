#string functions are functions that operate on strings. 

a = "hello world"
print(len(a))  # returns the length of the string

print(a.upper())  # converts the string to uppercase

print(a.lower())  # converts the string to lowercase

print(a.replace("hello", "hi"))  # replaces a substring with another substring

print(a.split())  # splits the string into a list of substrings

print(a.find("world"))  # finds the index of a substring

print(a.startswith("hello"))  # checks if the string starts with a substring

print(a.endswith("world"))  # checks if the string ends with a substring

print(a.count("l"))  # counts the number of occurrences of a substring

print(a.index("world"))  # finds the index of a substring, raises an error if not found

print(a.islower())  # checks if the string is in lowercase

print(a.isupper())  # checks if the string is in uppercase

print(a.swapcase())  # swaps the case of each character in the string

