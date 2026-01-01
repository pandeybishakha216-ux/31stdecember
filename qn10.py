secret_word = "python"
while True:
    guess = input("Guess the secret word (or 'quit' to exit): ").strip().lower()
    if guess == "quit":
        break
    elif guess == secret_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again")
        