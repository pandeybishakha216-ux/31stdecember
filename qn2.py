while True:
    vehicle = input("Enter vehicle name: ").strip().lower()
    if vehicle == "bus":
        print("finally the wait is over")
        break
    else:
        print("waiting")
        