# Rock, Paper, Scissors game in Python.
import random


result = {"User": 0, "Computer": 0}
rounds = 1
options = [
    "Rock",
    "Paper",
    "Scissors",
]

while rounds <= 5:
    print("Round:", rounds)
    try:
        inputVal = int(input("Enter your choice => 0: Rock, 1: Paper, 2: Scissors: "))
        if inputVal not in [0, 1, 2]:
            print("You have enterd wrong choice!")
            continue

    except ValueError:
        print("Please enter a valid Number!")
        continue

    user_choice = options[inputVal]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        print(
            "It is a Draw!",
            "Computer: ",
            computer_choice,
            ", " "User: ",
            user_choice,
        )

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result["User"] += 1
        print(
            "User won this Round",
            "Computer: ",
            computer_choice,
            ", " "User: ",
            user_choice,
        )
    else:
        result["Computer"] += 1
        print(
            "Computer won this Round",
            "Computer: ",
            computer_choice,
            ", " "User: ",
            user_choice,
        )
    rounds += 1

print("\nFinal Score: ", result)
if result["User"] == result["Computer"]:
    print("It is a Draw!")

elif result["User"] > result["Computer"]:
    print("User won!")

else:
    print("Computer won!")
