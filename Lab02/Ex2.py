def fizz_buzz(num):
    user_input = input("Enter a number: ")

    # check if input is valid integer
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a number.")
        return
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number < 0:
        print("The number must be zero or positive")
    else:
        print(number)