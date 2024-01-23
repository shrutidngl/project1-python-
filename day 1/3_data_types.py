# Python has a set of built-in datatypes.
# Numbers
# List
# String
# Tuple
# Dictionary
# Set
# Boolean

# Mutable and Immutable Datatypes

# Mutable => All those objects which can be altered after their creation are the mutable objects
# E.g. List, Dictionary, Set are mutable
# Immutable =>All those objects which cant be altered after their creation are the immutable objects
# E.g. Numbers, Boolean, Tuple and String are immutable


# Numbers
# Numbers can either be integer, float or complex

A = 12
print(type(A))  # int


A = 12.2
print(type(A))  # float

B = 2e2  # 2 * 10**2
print(B)  # 200.0
print(type(B))  # float

B = 2e-2  # 2 * 10** -2
print(B)  # 0.02
print(type(B))  # float

# If operation is carried with any of the float type then the result is always float
print(2 + 2.0)  # 4.0


A = 1 + 2j
print(A)  # 1+2j
print(type(A))  # complex