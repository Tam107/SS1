def daysOfWeek(x, m, y):
    y0 = y - (14 - m) // 12
    x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) -2

    d = (x + x0 + 31 * m0 //12 ) % 7
    if d == 1:
        return 'Monday'
    elif d == 2:
        return 'Tuesday'
    elif d == 3:
        return 'Wednesday'
    elif d == 4:
        return 'Thursday'
    elif d == 5:
        return 'Friday'
    elif d == 6:
        return 'Saturday'
    elif d == 0:
        return 'Sunday'
    else:
        return ''

print(daysOfWeek(29,9,2022))
