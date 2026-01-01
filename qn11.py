count = 0
while count < 3:
    phrase = input("Enter a phrase: ").strip().lower()
    if phrase == "good luck":
        count += 1
        if count < 3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times.")
    else:
        print(f"You entered: {phrase}")
        