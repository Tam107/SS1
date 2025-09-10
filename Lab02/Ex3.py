def gpaConverter(gpa):
    try:
        gpa = float(gpa)  # try to convert to float
    except (ValueError, TypeError):
        return "Please enter a gpa score in 10-point scale"

    if gpa < 0:
        return "Please enter a gpa score in 10-point scale"

    # Conversion rules
    if 9.0 <= gpa <= 10:
        return 4.0
    elif 8.5 <= gpa < 9.0:
        return 3.7
    elif 8.0 <= gpa < 8.5:
        return 3.5
    elif 7.0 <= gpa < 8.0:
        return 3.0
    elif 6.0 <= gpa < 7.0:
        return 2.5
    elif 5.5 <= gpa < 6.0:
        return 2.0
    elif 5.0 <= gpa < 5.5:
        return 1.5
    elif 4.0 <= gpa < 5.0:
        return 1.0
    elif 0 <= gpa < 4.0:
        return 0
    else:
        return "Please enter a gpa score in 10-point scale"
