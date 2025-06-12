#typecast is a function that converts a value to a specified type.
a = 1 # here a is an integer
b = 3.5 # here b is a float
c = "5" # here c is a string
d = True # here d is a boolean
# typecasting

b = type(a)
print(b) 
 # <class 'int'>, this shows the type of variable a
b = type(c)
print(b)

b = type(d)
print(b)

b = int(c)  # converts string to integer
print(b)  

e = "hello"
b=float(e)  # this will raise an error because "hello" cannot be converted to float

print(b)  # this will not be executed because of the error above