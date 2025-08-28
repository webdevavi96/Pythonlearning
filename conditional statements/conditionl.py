age = 18
if age >= 18:
    print("You are eligible to vote.")


is_logged_in = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")


is_logged_in = True

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")


username = "avi"
password = "1234"

if username == "avi":
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password")
else:
    print("User not found")


age = 24
message = "Adult" if age >= 18 else "Minor"
print(message)
