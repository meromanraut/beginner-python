"""Use comparison operator to find out 
whether ‘a’ given variable a 
is greater than
‘b’ or not. """

a=int(input("Enter a number for a: "))
b=int(input("Enter a number for b: "))
if a > b:
    print("a is greater than b")
elif a < b: 
    #elif is else if, it checks another condition if the first one is false
    print("a is less than b")
else:
    print("a is equal to b")
