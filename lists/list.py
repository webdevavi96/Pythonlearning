fruits = ["apple", "banana", "cherry"]

# Indexing
print(fruits[0])  # apple
print(fruits[-1])  # cherry

# Slicing
print(fruits[1:])  # ['banana', 'cherry']
print(fruits[:2])  # ['apple', 'banana']
print(fruits[0:1])  # ['apple']
# Add
fruits.append("mango")  # ['apple', 'banana', 'cherry', 'mango']
fruits.insert(1, "grape")  # ['apple', 'grape', 'banana', 'cherry', 'mango']

# Remove
fruits.remove("banana")  # removes first 'banana'
last = fruits.pop()  # removes last item
print(fruits)

#sorting a list
fruits.sort()
print(fruits) #['apple', 'cherry', 'grape']
