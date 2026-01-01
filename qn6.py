import random

number = random.randint(1, 10)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number:
            print("guess higher")
        elif guess > number:
            print("guess lower")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
        