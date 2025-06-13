"""Write a python program to calculate 
the square of a number entered by
 the user."""

a = float(input("Enter any number to find the square: "))
sq= a**2 #in python a^2 is not square, it is bitwise XOR
#we can aslo use a*a to find the square

print("The square is:", sq)