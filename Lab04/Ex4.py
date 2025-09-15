def setOperation(list1, list2, operator):
    if operator == 'x':
        return [item for item in list1 if item in list2]
    elif operator == '/':
        return [item for item in list1 if item not in list2]
    elif operator == 'u':
        return [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]
    else:
        return []