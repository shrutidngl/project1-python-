# List are sequential datatypes (iterables) in python enclosed in big brackets => []
# They are the mutable datatypes

# Creating list in python
A = []  # empty list
B = []  # empty list. list() is a built-in function to create a list

C = [1, 2, 3]  # Non-empty list
# List elements can be of different datatypes.

D = [1, 2.1, "hello", [1, 2], (4, 5), []]

# Unlike in list, arrays elements must be homogenous


# Accessing list elements
# List elements can be accessed using indexing or slicing

# Indexing
VOWELS = ["a", "e", "i", "o", "u"]
print(VOWELS[0])  # a
print(VOWELS[4])  # u 
print(VOWELS[-1])  # u
print(VOWELS[-4])  # e


# Slicing
DATA = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(DATA[0:7])  # ["a", "b", "c", "d", "e", "f", "g"]
print(DATA[7:])  # ["h", "i", "j"]
print(DATA[3:8])  # ["d", "e", "f", "g", "h"]
print(DATA[:5])  # ["a", "b", "c", "d", "e"]

print(DATA[:-8])  # ["a", "b"]
print(DATA[-4:])  # ["g", "h", "i", "j"]
print(DATA[-8:-2])  # ["c", "d", "e", "f", "g", "h"]
print(DATA[-3:-7])  # []
print(DATA[2:9:2])  # ["b", "d", "f", "h"]


print(DATA[3:9]) #["d", "e", "f", "g", "h", "i"]
print(DATA[8:2]) #[]
print(DATA[5:]) #["f", "g", "h", "i", "j"]
print(DATA[:4])  # ["a", "b", "c", "d"]
print(DATA[-9:-3]) # ["b", "c", "d", "e", "f", "g"]
print(DATA[-8:8]) # ["c", "d", "e", "f", "g","h"]
print(DATA[9:-7]) # []
print(DATA[-4:-9]) # []


# List Operations

# Concatenation (+)
A = [1, 2, 3]
B = [4, 5, 6]
RESULT = A + B
print(RESULT)  # [1, 2, 3, 4, 5, 6]


# Repetition/broadcast Operation (*)
A = [1, 2]
print(A * 3)  # [1, 2, 1, 2, 1, 2]


# Membership Operation ("in" and "not in")
print("a" in {"a", "e", "i"})
  # True
print("e" not in ["a", "e", "i"])  # False