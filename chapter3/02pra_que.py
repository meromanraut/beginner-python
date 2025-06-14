"""Write a program to fill in a letter template given below with name and date. 
letter = ''' Dear <|Name|>, You are selected! <|Date|> '''"""

letter = ''' Dear <|Name|>,
You are selected! <|Date|> '''
name = input("Enter your name: ")
date = input("Enter the date: ")
letter = letter.replace("<|Name|>", name) # Replacing placeholder with user input
letter = letter.replace("<|Date|>", date) # Replacing placeholder with user input
print(letter)  


print("\n \n \nsecond method")
# Using f-string for formatted output

a = input("Enter your name: ")
b = input("Enter the date: ")

print(f"Dear {a},\nYou are selected! {b}")

