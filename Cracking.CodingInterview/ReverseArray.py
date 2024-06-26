#Reverse int array complex O(N)
def reverse(arr):
    for i in range(len(arr) // 2):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp



arr = [5, 3, 7, 2 ,9]
reverse(arr)
print(arr)