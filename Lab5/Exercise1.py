from collections import defaultdict

def itemGrouping(inputList)-> dict:
    result = {}
    for item in inputList:
        if item not in result:
            result[item] = []
        result[item].append(item)
    return result

def itemGrouping2(inputList)-> dict:
    result = defaultdict(list)
    for item in inputList:
        result[item].append(item)
    return dict(result)

check = [2,2,2,4,5,3,4,2,4,5]
check = defaultdict(list)
print(check)

print(itemGrouping2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))