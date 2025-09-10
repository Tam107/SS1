def readOneDigit(number):
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    else:
        return 'ten'


def readTwoDigits(number):
    def readFromElevenToNineteen(num):
        if num == 11:
            return 'eleven'
        elif num == 12:
            return 'twelve'
        elif num == 13:
            return 'thirteen'
        elif num == 14:
            return 'fourteen'
        elif num == 15:
            return 'fifteen'
        elif num == 16:
            return 'sixteen'
        elif num == 17:
            return 'seventeen'
        elif num == 18:
            return 'eighteen'
        else:
            return 'nineteen'

    def readMultiplyByTen(num):
        if num == 20:
            return 'twenty'
        elif num == 30:
            return 'thirty'
        elif num == 40:
            return 'forty'
        elif num == 50:
            return 'fifty'
        elif num == 60:
            return 'sixty'
        elif num == 70:
            return 'seventy'
        elif num == 80:
            return 'eighty'
        else:
            return 'ninety'

    resultText = ''
    if (number < 10):
        resultText = readOneDigit(number)
    elif (number < 20):
        resultText = readFromElevenToNineteen(number)
    elif (number % 10 == 0):
        resultText = readMultiplyByTen(number)
    else:
        resultText = readMultiplyByTen(number - number % 10) + ' ' + readOneDigit(number % 10)
    return resultText


def readFourDigits(number):
    first_digit = number // 1000
    second_digit = (number % 1000) // 100
    two_digits_left = number % 100

    resultText = ''

    if (two_digits_left != 0):
        resultText = readTwoDigits(two_digits_left)
    if (second_digit != 0):
        if (resultText != ''):
            resultText = readOneDigit(second_digit) + ' hundred and ' + resultText
        else:
            resultText = readOneDigit(second_digit) + ' hundred'
    if (first_digit != 0):
        if (resultText != ''):
            resultText = readOneDigit(first_digit) + ' thousand and ' + resultText
        else:
            resultText = readOneDigit(first_digit) + ' thousand'

    return resultText