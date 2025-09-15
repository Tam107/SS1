def checkMaxNumber(num):
    return num % 100

def checkMaxNumber(a: str, b: str) -> int:
    if a + b > b + a:
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
    return int(result)   # convert về int để bỏ 0 thừa


print(maxPermutation([8, 4, 2, 9, 5, 6, 1, 0]))




