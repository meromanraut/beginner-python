#list in python are ordered collection oof items that can be changed
# and allow duplicate values.
# Lists are defined by having values between square brackets [].

a = [1, 2, 3, 4, 8, 5]  
b = ["apple", "banana", "cherry"]
c = [1, "apple", 3.5, True] 
d = []  
 
print(a)  
print(b)
print(c)
print(d)


a.append(6) 
print(a)  # [1, 2, 3, 4, 5, 6] 
b.insert(2,"orange") 
#b.append(2,"orange")  # this will raise an error
print(b)
c.pop(1)  # removes the item at index 1
print(c)  
c.remove(3.5)  # removes the first occurrence of 3.5
print(c)  
a.reverse()  # reverses the list
print(a)  
a.sort()  # sorts the list in ascending order
print(a) 