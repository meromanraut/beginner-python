#Write a program to store seven fruits in a list entered by the user

a = []
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    a.append(fruit)
print("The list of fruits is:", a)