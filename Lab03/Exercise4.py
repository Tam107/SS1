def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def countPrime(left, right):
    count = 0
    for i in range(left, right + 1):
        if isPrime(i):
            count += 1
    return count

print(countPrime(1, 10))
print(countPrime(15, 20))