import random
username = "admin"
password = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    input_user = input("Enter username: ").strip()
    input_pass = input("Enter password: ").strip()
    
    if input_user == username and input_pass == password:
        print("Login successful")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Invalid credentials, try again. ({max_attempts - attempts} attempts left)")
        else:
            print("Too many failed attempts.")

