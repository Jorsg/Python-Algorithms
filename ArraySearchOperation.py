#Array Search Operation
#Algorithm

#1. Start
#2. Set J = 0
#3. Repeat steps 4 and 5 while J < N
#4. IF LA[J] is equal ITEM THEN GOTO STEP 6
#5. Set J = J + 1
#6. Print J, ITEM
#7. Stop

def findElement(arr, n, value):
    for i in range(n):
        if(arr[i] == value):
            return i
            
    return -1

if __name__ == '__main__':
    LA = [1,3,5,7,8]
    print("Array element are:")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])

    value = 5
    n = len(LA)
    #element found using search operation
    index = findElement(LA, n, value)
    if index != -1:
        print("Element", value, "Found at position = " + str(index + 1))
    else:
        print("Element not found")    


