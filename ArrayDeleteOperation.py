#Array Delete Operation
#Algorithm
#1. Start
#2. Set J = k
#3. Repeat steps 4 and 5 while J < N
#4. Set LA[J] = LA[J + 1]
#5. Set J = J + 1
#6. N = N - 1
#7. Stop

if __name__ == '__main__':
    LA = [0,0,0]
    n = len(LA)

    print("Array Before Deletion: ")
    for x in range(len(LA)):
        LA.append(x)
        LA[x] = x + 3
        print("LA", [x], " = ", LA[x])
    #delete the value if exists
    # 
    for x in range(1, n-1):
        LA[x] = LA[x+1]
        n = n - 1
    
    print("Array after Deletion:")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])
    



