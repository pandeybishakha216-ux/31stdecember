current_floor = 1
print(f"Elevator is on floor {current_floor}")

while True:
    try:
        target = input("Enter destination floor (or 0 to exit): ").strip()
        target_floor = int(target)
        
        if target_floor == 0:
            print("Goodbye!")
            break
        
        if target_floor == current_floor:
            print(f"You are already on floor {current_floor}.")
        elif target_floor > current_floor:
            print(f"Going up from floor {current_floor} to floor {target_floor}")
            current_floor = target_floor
        else:
            print(f"Going down from floor {current_floor} to floor {target_floor}")
            current_floor = target_floor
            
    except ValueError:
        print("Please enter a valid floor number.")
        