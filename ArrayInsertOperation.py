# Array - Insert Operation

# Algorithm
#1. Start
#2. Create an Array of a desired datatype and size
#3. Initialize a variable 'i' as 0
#4. Enter the element at ith index of the array
#5. Increment i by 1
#6. Repeat Steps 4 & 5 until the end of the array
#7. Stop

def insert(arr, element):
    arr.append(element)


if __name__ == '__main__':
    LA = [0,0,0]
    x = 0

    print("Array Before Insertion: ")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])

    print("Inserting Elements....")

    for x in range(len(LA)):
        LA.append(x)
        LA[x] = x + 1
    print("Array after Inserting: ")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])    

