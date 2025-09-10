def sentinelInput():
    total = 0
    count = 0
    while True:
        try:
            user_input = int(input("Enter a positive integer: ").strip())
        except ValueError:
            print("Please enter a positive number")
            continue

        if user_input < 0:
            print("The number must be positive")
            continue

        if user_input == 0:  # sentinel: stop and compute
            break

        total += user_input
        count += 1

    if count == 0:
        return 0

    avg = total / count
    return float(f"{avg:.2f}")



print(sentinelInput())
