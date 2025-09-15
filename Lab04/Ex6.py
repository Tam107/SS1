from functools import cmp_to_key

def checkMaxNumber(a: str, b: str) -> int:
    if a + b > b + a:
        result = a +b
        return -1   # a trước
    elif a + b < b + a:
        return 1    # b trước
    else:
        return 0

def maxPermutation(lst: list) -> int:
    # Chuyển tất cả sang string
    nums = list(map(str, lst))
    # Sort với custom comparator
    nums.sort(key=cmp_to_key(checkMaxNumber))
    # Ghép lại thành chuỗi
    result = ''.join(nums)
    return int(result)   # c

# print(maxPermutation([8, 4, 2, 9, 5, 6, 1, 0]))
print(maxPermutation([320, 400, 41, 4, 745, 9]))