def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    user_input = input("Enter a number to check if prime (or 'exit'): ").strip()
    if user_input.lower() == "exit":
        break
    try:
        num = int(user_input)
        if is_prime(num):
            print("The number is prime.")
        else:
            print("The number is not prime.")
    except ValueError:
        print("Please enter a valid number.")