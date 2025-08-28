a = [1, 2]
b = [1, 2]
c = a

print(a is b)       # False (different memory locations)
print(a is c)       # True (same memory location)
print(a is not b)   # True
a = [1, 2]
b = [1, 2]
c = a

print(a is b)       # False (different memory locations)
print(a is c)       # True (same memory location)
print(a is not b)   # True
