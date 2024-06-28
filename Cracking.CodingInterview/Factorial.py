def factorial(num):
    fact = 1
    if num == 0:
        return 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# use 
print(factorial(0))  # Expected output: 1
print(factorial(1))  # Expected output: 1
print(factorial(5))  # Expected output: 120
print(factorial(7))  # Expected output: 5040
