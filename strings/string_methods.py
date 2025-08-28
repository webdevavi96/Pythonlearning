s = " Hello Python   "
words = ["Hello", "this", "is", "Python"]
print(s)
print(s.upper())  # converts the string into upper case
print(s.lower())  # converts the string into lower case
print(s.split())  # It splits the string into a list ["Hello", "Python"]
print(s.strip())  # Removes extra spaces
print(len(s))  # It will tell the total length of string
print(len(s.strip()))  # It will tell the length of string withput extra blank spaces
print(s.replace("Python", "World!"))  # It will reoplace Python with World!
print(
    s.startswith("H")
)  # It will print False because the string is starting with blank spaces
print(s.endswith(" ")) #It will print True becuase the string ends with blank space
print(s.find("ho"))  #tells the position of the charecter into the string
print(" ".join(words)) #joins all the charecters to make a string.