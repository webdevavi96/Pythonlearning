user = {
    "name": "Avinash",
    "age": 22,
    "is_active": True
}

print(user["name"])        # Avinash
print(user.get("email"))   # None (doesn't throw error if key is missing)

user["email"] = "avi@example.com"   # add new key
user["age"] = 23                    # update value

print(user)   #{'name': 'Avinash', 'age': 23, 'is_active': True, 'email': 'avi@example.com'}
print(user.get("email"))  #avi@example.com


# for key in user:
#     print(key, user[key])

# # Or:
# for key, value in user.items():
#     print(f"{key}: {value}")



user.pop("age")         # removes and returns value
del user["is_active"]   # deletes the key-value pair
user.clear()            # clears all items
print(user) #{} because the dictonery is empty