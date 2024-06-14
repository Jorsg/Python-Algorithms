def MinOperationSolut(numArry, k):
    cont = 0
    for i in range(0, len(numArry)):
        if numArry[i] < k:
            cont += 1
    return cont

print(MinOperationSolut([1, 1, 2, 4, 9], 9))

