a = 5    # 0101
b = 3    # 0011

print(a & b)   # 1 (0001)
print(a | b)   # 7 (0111)
print(a ^ b)   # 6 (0110)
print(~a)      # -6 (inverts all bits)
print(a << 1)  # 10 (1010, left shift)
print(a >> 1)  # 2  (0010, right shift)
