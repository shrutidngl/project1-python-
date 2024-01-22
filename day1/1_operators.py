# Operators are the special symbols which are used ro carry out arithmetical and logical operations.
# Like in any other language python also has it's set of operators

# Arithmetic Operators
# Logical Operators
# Relational Operators
# Assignment Operators
# Membership Operators
# Identity Operators


# Arithmetic Operators (+, -, /, *, **, %)
A = 1  # Python statement
B = 2  # Python statement

RESULT = A + B
print("The result of the sum is", RESULT)

RESULT = B**2

print(RESULT)   # 4

RESULT = 5 % 2
print(RESULT)   # 1

RESULT = 5 / 2
print(RESULT)  # 2.5


# Relational / Comparison Operators (>, <, >=, <=, ==, !=)
# The result of comparison operations are either True or False

A = 20
B = 15
print(A > B)  # True
print(A < B)  # False
print(A == B)  # False
print(A >= B)  # True
print(A <= B)  # False
print(A != B)  # True


# Logical Operators (and, or, not)
# The result of logical operations are either True or False

print(True)  # True
print(False)  # False
print(False)  # False
print(False)  # False

print(True)  # True
print(True)  # True
print(True)  # True
print(False)  # False

print(False)  # False
print(True)  # True


A = 1
B = 15
C = 15

if A > B or B == C:
    print("Hello World")


# Assignment Operator (=, +=, -=, *=, /=)
MESSAGE = "Hello World"
B = 5
B = B + 5
print(B)  # 10

B += 5
print(B)  # 15

B -= 5
print(B)  # 10


# Membership Operators ('in' and 'not in')
# The result of membership operation is also True or False
# Membership operators are used in the sequential data (iterables) e.g. list, array, tuple etc.
VOWELS = ["a", "e", "i", "o", "u"]

print("a" in VOWELS)  # True
print("A" in VOWELS)  # False
print("A" not in VOWELS)  # True
print("a" not in VOWELS)  # False


# Identity Operator ('is' and 'is not')
# The result of identity operations are also in True/False
# It checks whether the two objects are same or not

A = 4
B = 4
print(A is B)  # True, Same object

A = []
B = []
print(A is B)   # False, different object