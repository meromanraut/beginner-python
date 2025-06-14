#Write a program to sum a list with 4 numbers.

a = []
for i in range(4):
    num = float(input(f"Enter number {i + 1}: "))
    a.append(num)
sum_of_numbers = sum(a)
print("The sum of the numbers is:", sum_of_numbers)

