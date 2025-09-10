def inputValidation():
    while True:
        try:
            userInput = int(input("Enter a odd integer from 1 to 50: "))
            if userInput < 1 or userInput > 50 or userInput % 2 == 0:
                print("The number must be an odd number from 1 to 50")
                continue
            break
        except ValueError:
            print("Please enter an integer")
    return userInput

print(inputValidation())
