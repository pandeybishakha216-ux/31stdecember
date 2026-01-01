while True:
    age_input = input("Enter your age (or 'stop' to exit): ").strip()
    if age_input.lower() == "stop":
        break
    if age_input.isdigit():
        age = int(age_input)
        if age < 18:
            print("You are a minor.")
        elif 18 <= age <= 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    else:
        print("Please enter a valid number or 'stop'.")
