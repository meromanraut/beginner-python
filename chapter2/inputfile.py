a = input("Enter a number: ")
b = input("Enter another number: ")

print("You entered:", a)
print("You entered:", b)
print("both number are:", a, b)
print("The sum of the two numbers is:", a+b)  #this will concatenate the two strings
# To perform addition, we need to convert the inputs to integers or floats

print("The sum of the two numbers is:", int(a) + int(b))  # this will add the two integers
print("The sum of the two numbers is:", float(a) + float(b))  # this will add the two floats

# Note: The input function returns a string, so we need to convert it to an integer or float for arithmetic operations.
