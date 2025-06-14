#Write a program to detect double space in a string and remove it 


a= input("Enter a string: ")
if "  " in a:
    print("Double space detected.")
    print(a.find("  "))  # Find the index of the first occurrence of double space
    # Remove double spaces
    a = a.replace("  ", " ")
    print("\n String after removing double spaces:\n", a)

else:
    print("No double space detected.")

# # Remove double spaces
# a = a.replace("  ", " ")
# print("String after removing double spaces:", a)