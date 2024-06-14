def  fibonacci(num):
    if(num <= 0):
        return []
    if(num == 1):
        return [0]
    elif num == 2:
        return [0,1]

    fib_sequence = [0, 1]
    for i in range(2, num):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)


    return fib_sequence


print(fibonacci(20))