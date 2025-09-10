def maxFiveNumbers(num1, num2, num3, num4, num5):
    maxFive = num1
    if num1 > maxFive:
        maxFive = num1
    if num2 > maxFive:
        maxFive = num2
    if num3 > maxFive:
        maxFive = num3
    if num4 > maxFive:
        maxFive = num4
    if num5 > maxFive:
        maxFive = num5

    return maxFive

print(maxFiveNumbers(4, 8, 6, 1, 7)
)