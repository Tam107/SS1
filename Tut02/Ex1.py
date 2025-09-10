#  year is a leap year if it is divisible by 400 or it is divisible by 4 and is not divisible by 100.
# Write a program to get an integer represented a year in calendar. Then the program will do the following:
# If user doesn't enter an integer, the program will display: Enter an integer, please
# If user enters a zero or negative number, the program will display: The number must be positive
# If user enters a positive integer, the program will print YES if the year is a leap year or NO if the year is not a leap year.
# Please refer to the example table about the input and output of the program.




try:
    user_input = int (input("Enter a year: "))
    if user_input <= 0:
        print("The number must be positive")
    elif user_input % 400 == 0 or user_input % 4 == 0 and user_input % 100 !=0:
        print("YES")
    else:
        print("NO")
except ValueError:
    print("Enter an integer, please")

