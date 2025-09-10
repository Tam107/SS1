number = int(input("Enter a number (from 0 to 999): "))
third_number = number // 100
second_number = (number - third_number * 100) // 10
first_number = number - third_number * 100 - second_number * 10
sum_digits = first_number + second_number + third_number
print("The sum of digits is", sum_digits)