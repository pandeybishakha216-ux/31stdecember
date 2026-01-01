password = "open sesame"
while True:
    guess = input("Enter password: ").strip()
    if guess == password:
        print("Access granted!")
        break
    else:
        print("Wrong password, try again.")
