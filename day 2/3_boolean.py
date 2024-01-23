# True and False are the boolean datatypes
# True and False itself are the keywords to represent True and False in Python

# Operations yielding boolean result
# Logical operations (and, or, not)
# Relational Operations (>, <, >=, <=, ==, !=)
# Membership Operation (in and not in)
# Identity Operation (is and is not)


# Boolean datatypes are the subclass of integer datatypes in python
# True is equals to 1
# False is equals to 0

A = True + True
print(A)  # 2
B = 50 * False
print(B)  # 0


# Concept of Truthy and Falsy in python Boolean

# Truthy
# All the non-empty datatypes along with True itself and non-zero number are the truthy data.

A = 3
B = [1, 2]
C = (1, 2)
D = {4, 5}
E = {"a": 1, "b": 2}
F = 3.4
G = "hello"
H = True
print(bool(A))  # True
print(bool(B))  # True
print(bool(C))  # True
print(bool(D))  # True
print(bool(E))  # True
print(bool(F))  # True
print(bool(G))  # True
print(bool(H))  # True


# falsy
A = 0
B = 0.0
C = []
D = ()
E = ""
F = {}
G = set()
H = False
I = None
print(bool(A))  # False
print(bool(B))  # False
print(bool(C))  # False
print(bool(D))  # False
print(bool(E))  # False
print(bool(F))  # False
print(bool(G))  # False
print(bool(H))  # False