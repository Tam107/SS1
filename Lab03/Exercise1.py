def isPrime(num):
    for i in range(2, num / 2):
        if num % i == 0:
            return False
    return True

print(isPrime(15))
print(isPrime(29))
print(isPrime(99))