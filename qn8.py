mport random

while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    correct_answer = num1 * num2
    
    user_input = input(f"What is {num1} × {num2}? (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == "exit":
        print("Quiz ended.")
        break
    
    try:
        answer = int(user_input)
        if answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect, try again.")
    except ValueError:
        print("Please enter a number or 'exit'.")