import random


def genRandomIntegers(left, right):
    generated_numbers = []
    count_divisible_by_5 = 0

    while count_divisible_by_5 < 5:
        number = random.randint(left, right)
        generated_numbers.append(number)

        if number % 5 == 0:
            count_divisible_by_5 += 1

    return ' '.join(map(str, generated_numbers))