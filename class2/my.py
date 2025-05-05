# range type
# for num in range(1,20):
    # print(num)
    # print(chr(99))
    # a=9
    # b=a
    # b=10
    # c=9
    # print(c)
    # print(type(c))
    # print(str(c))
    # c : int =8
# print(id(a))
# print(id(b))
# if type(c) == int:
#     print("c is an iteger")
# else:
# print("c is not an integer")
# print(isinstance(type(c),int))
# print(isinstance(type(c),float))
# Operations
# +
# -
# * 
# /
# %
# //
# **
# 2**2 =4
# Logical Not Operater
# a=True
# b=8
# print(not a)
# BitWise Not(~)
# Comparsion Operater
# ==
# >=
# <=
# >
# <
# !=
# x: int = 10
# y:int =5
# print()
# print()
# print()
# print()
# logical_Operaters
# and = True and True and False
# or = True or True or False
# Assigment Operaters
# =
# +=
# -=
# Identety Operater
# is
# is not
# a =True
# print(a is True)
# print(a is not True)
# MemberShip Operater
# names :list[str]= ["Anas","Umar","Uzair"]
# result = "Anas" in names
# result1 = "Anas" not in names
# print(result)
# print(result1)
# del result1
# Assigement
# 1> Python Operaters Complete Operater 7 types

# Arithmetic operators
# Define two numbers
a = 10
b = 5

# Perform arithmetic operations
print("Addition:", a + b)        # 10 + 5 = 15
print("Subtraction:", a - b)     # 10 - 5 = 5
print("Multiplication:", a * b)  # 10 * 5 = 50
print("Division:", a / b)        # 10 / 5 = 2.0
print("Modulus:", a % b)         # 10 % 5 = 0
print("Exponentiation:", a ** b) # 10^5 = 100000
print("Floor Division:", a // b) # 10 // 5 = 2

# Assignment operators
# Simple Assignment
x = 10  
print("x =", x)  # Output: 10

# Addition Assignment
x += 5  # Equivalent to: x = x + 5
print("x += 5 ->", x)  # Output: 15

# Subtraction Assignment
x -= 3  # Equivalent to: x = x - 3
print("x -= 3 ->", x)  # Output: 12

# Multiplication Assignment
x *= 2  # Equivalent to: x = x * 2
print("x *= 2 ->", x)  # Output: 24

# Division Assignment
x /= 4  # Equivalent to: x = x / 4
print("x /= 4 ->", x)  # Output: 6.0

# Modulus Assignment
x %= 5  # Equivalent to: x = x % 5
print("x %= 5 ->", x)  # Output: 1.0

# Exponentiation Assignment
x **= 3  # Equivalent to: x = x ** 3
print("x **= 3 ->", x)  # Output: 1.0

# Floor Division Assignment
x //= 2  # Equivalent to: x = x // 2
print("x //= 2 ->", x)  # Output: 0.0
# Comparison operators
# Define two numbers
a = 10
b = 5

# Comparison operations
print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to

# Logical operators
# Define two boolean values
a = True
b = False

# Logical AND
print("a and b:", a and b)  # False (Both must be True)

# Logical OR
print("a or b:", a or b)    # True (At least one must be True)

# Logical NOT
print("not a:", not a)      # False (Reverses True to False)
print("not b:", not b)      # True (Reverses False to True)

# Identity operators
# Define two variables
a = 10
b = 10
c = 5

# Identity operators
print("a is b:", a is b)    # True (Same memory location for immutable objects)
print("a is c:", a is c)    # False (Different values)
print("a is not c:", a is not c)  # True (a and c are different)

# Membership operators
# Define a list
numbers = [1, 2, 3, 4, 5]

# Membership operators
print(3 in numbers)     # True (3 is in the list)
print(10 in numbers)    # False (10 is not in the list)
print(6 not in numbers) # True (6 is not in the list)

# - Bitwise operators
# Define two numbers
a = 5  # (Binary: 0101)
b = 3  # (Binary: 0011)

# Bitwise operations
print("a & b:", a & b)  # AND -> 0101 & 0011 = 0001 (1)
print("a | b:", a | b)  # OR  -> 0101 | 0011 = 0111 (7)
print("a ^ b:", a ^ b)  # XOR -> 0101 ^ 0011 = 0110 (6)
print("~a:", ~a)        # NOT -> ~(0101) = -(0101+1) = -6
print("a << 1:", a << 1) # Left Shift  -> 0101 << 1 = 1010 (10)
print("a >> 1:", a >> 1) # Right Shift -> 0101 >> 1 = 0010 (2)
