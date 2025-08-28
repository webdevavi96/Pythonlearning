import random

n = random.randint(1, 10)
total_guesses = 1
guesses = 1
num = -1

while num != n:
    try:
        num = int(input("Guess the number: "))

    except e as e:
        print("Please enter a valid number..")
        print(f"{5 - guesses} left.")
        guesses += 1

    if num == n:
        print(f"You guessed the Number {n} in {guesses} guesses, {5 - guesses} left.")

    elif guesses == 5:
        print(f"Your don't have any guesses left. the number was {n}.")
        num = n
        
    elif n > num:
        print(f"Try guessing lower number than {num}. Total {5 - guesses} guesses left.")
        guesses += 1
        
    else:
        print(f"Try guessing higher number than {num}. Total {5 - guesses} guesses left.")
        guesses += 1
        