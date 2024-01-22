# Strings are the sequence of characters in Python. They are also the iterables (sequence of data)

def _pyrefact_abstraction_1():
    data = "I'm learning Python"
    data = 'He said, "Python is high level language"'
    data = "Python is a high level language"
    return data
# character itself is also a string in Python
# Strings are enclosed either in double quotes ("") or single quotes ('') or triple quotes ("""""" or '''''')
# String is an immutable datatype

# Creating strings
A = ""  # empty string
B = ""
  # empty string
C = """"""  # empty string
D = """"""
  # empty string

E = "Hello World"  # non-empty string
F = "Hello World"
  # non empty string
G = """
I'm learning Python.
Python is a high level language
"""
H = """
I'm learning Python.
Python is a high level language
"""

DATA = _pyrefact_abstraction_1()


# Accessing string items
# String items can also be accessed using indexing and slicing


# Indexing

print(DATA[0])  # P
print(DATA[6])  # ' '
print(DATA[-1])  # e
print(DATA[-8])  # l


# Slicing
print(DATA[3:8])  # hon i
print(DATA[7:2])  # ''
print(DATA[:7])  # Python
print(DATA[9:])  # ' a high level language'
print(DATA[-8:-2])  # langua
print(DATA[-3:-7])  # ''
print(DATA[:-7])  # Python is a high level l
print(DATA[-5:])  # guage


# We cannot update string elements because string is an immutable datatype

DATA = "I am learning"
DATA[5] = "L"  # This raises error. We can't change the particular position of a string data.
del DATA[5]  # This is also not possible

# But we can delete the string object
# del data   # It deletes the string object


# String Special Operators

# Concatenation
A = "Hello"
B = "World"
RESULT = A + B
print(RESULT)


# Repetition 
B = "World"
print(A * 3)

# Membership 


# len() is a built-in  function in python that gives length of an iterable
# It can give the length of strings, lists, tuple, dictionary, set and any other iterable

print(len("Hello"))  # 5