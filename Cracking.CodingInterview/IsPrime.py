import math
def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    for x in range(2, int(math.sqrt(n)) + 1):
        if (n % x == 0):
           return False

    return True

#Example usage
print(isPrime(33))
print(isPrime(3))
print(isPrime(1))
print(isPrime(5))