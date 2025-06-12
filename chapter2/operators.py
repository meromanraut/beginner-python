#assigment operators "=, +=, -=, *=, /=, //=, %=, **="
#arithmetic operators "+, -, *, /, //, %, **"
#comparison operators "==, !=, >, <, >=, <=, is, is not"
#logical operators "and, or, not"
#bitwise operators "&, |, ^, ~, <<, >>"

# arithmetic operators

print("Arithmetic Operators")

a = 10
b = 3
c = 5-2 
print(c)  # subtraction
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b)  # floor division
print(a % b)  # modulus
print(a ** b)  # exponentiation


# assigment operators
print("\nAssignment Operators")
 

a = 10
b = 3
a += b  # a = a + b
print(a)  # 13
a -= b  # a = a - b
print(a)  # 10
a *= b  # a = a * b
print(a)  # 30
a /= b  # a = a / b
print(a)  # 10.0
a //= b  # a = a // b

print(a)  # 3.0
a %= b  # a = a % b
print(a)  # 0.0
a **= b  # a = a ** b
print(a)  # 1.0

# comparison operators
print("\nComparison Operators")
a = 10
b = 3
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False
print(a is b)  # False
print(a is not b)  # True

# logical operators
print("\nLogical Operators")
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False
print(not b)  # True

# bitwise operators
print("\nBitwise Operators")
a = 10  # 1010 in binary
b = 3   # 0011 in binary
print(a & b)  # Bitwise AND: 0010 in binary, which is 2 in decimal
print(a | b)  # Bitwise OR: 1011 in binary, which is 11 in decimal
print(a ^ b)  # Bitwise XOR: 1001 in binary, which is 9 in decimal
print(~a)  # Bitwise NOT: Inverts all bits, resulting in -11 in decimal
print(a << 1)  # Left shift: 10100 in binary, which is 20 in decimal
print(a >> 1)  # Right shift: 0101 in binary, which is 5 in decimal

