#Creating Tupels

person = ("Avinash", 22, "India")
t1 = (1, 2, 3)
t2 = ("apple", True, 3.14)
t3 = ()                # empty tuple
t4 = (5,)              # ⚠️ single-value tuple MUST have comma!


#Accessing tupels

print(person[0])   # Avinash
print(person[-1])  # India


# for item in person:
#     print(item)

t = (1, 2, 3, 2, 1)
print(t.count(2))     # 2
print(t.index(3))     # 2


# Packing
user = ("Avinash", 22, "India")

# Unpacking
name, age, country = user
print(name, age, country)
