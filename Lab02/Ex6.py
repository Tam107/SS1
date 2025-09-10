def readOneDigit(n: int) -> str:
    words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine", "ten"
    ]
    return words[n]


def readTwoDigits(n: int) -> str:
    if 0 <= n <= 10:
        return readOneDigit(n)

    # 11–19 special cases
    if 11 <= n <= 19:
        if n == 11: return "eleven"
        if n == 12: return "twelve"
        if n == 13: return "thirteen"
        if n == 14: return "fourteen"
        if n == 15: return "fifteen"
        if n == 16: return "sixteen"
        if n == 17: return "seventeen"
        if n == 18: return "eighteen"
        if n == 19: return "nineteen"

    tens_words = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    tens, ones = divmod(n, 10)

    if ones == 0:
        return tens_words[tens]
    else:
        return tens_words[tens] + " " + readOneDigit(ones)


def readThreeDigits(n: int) -> str:
    """Helper to read numbers 0–999 correctly with 'and'."""
    hundreds = n // 100
    last_two = n % 100
    parts = []

    if hundreds > 0:
        if last_two == 0:
            return readOneDigit(hundreds) + " hundred"
        else:
            return readOneDigit(hundreds) + " hundred and " + readTwoDigits(last_two)
    else:
        if last_two == 0:
            return ""
        else:
            return readTwoDigits(last_two)


def readFourDigits(n: int) -> str:
    """Read numbers 0–9999 in words."""
    if n < 1000:
        return readThreeDigits(n)

    thousands = n // 1000
    remainder = n % 1000

    if remainder == 0:
        return readOneDigit(thousands) + " thousand"
    else:
        return readOneDigit(thousands) + " thousand and " + readThreeDigits(remainder)


